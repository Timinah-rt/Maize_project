import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error
from xgboost import XGBRegressor
import warnings
warnings.filterwarnings("ignore")

FEATURES_DIR = Path(__file__).parent.parent.parent / "data" / "features"
MODELS_DIR = Path(__file__).parent.parent.parent / "models"


def mase(y_true, y_pred, y_train):
    n = len(y_true)
    denom = np.mean(np.abs(np.diff(y_train))) if len(y_train) > 1 else 1.0
    if denom == 0:
        denom = 1.0
    return np.mean(np.abs(y_true - y_pred)) / denom


def directional_accuracy(y_true, y_pred):
    true_dir = np.sign(y_true)
    pred_dir = np.sign(y_pred)
    correct = true_dir == pred_dir
    correct = correct[true_dir != 0]
    if len(correct) == 0:
        return 0.5
    return correct.mean()


def smape(y_true, y_pred):
    denom = (np.abs(y_true) + np.abs(y_pred)) / 2
    denom = np.where(denom == 0, 1e-10, denom)
    return np.mean(np.abs(y_true - y_pred) / denom) * 100


class MaizePriceForecaster:
    def __init__(self, target_counties=None):
        if target_counties is None:
            target_counties = ["Kiambu", "Kirinyaga", "Mombasa", "Nairobi", "Uasin-Gishu"]
        self.target_counties = target_counties
        self.pooled_xgb = None

    def prepare_data(self, panel):
        df = panel.sort_values(["county", "week_start"]).copy()
        df["price_change"] = df.groupby("county")["price"].diff(1)
        df["price_change_lag_1w"] = df.groupby("county")["price_change"].shift(1)
        df["price_change_lag_2w"] = df.groupby("county")["price_change"].shift(2)
        df["price_change_ma_4w"] = df.groupby("county")["price_change"].transform(
            lambda x: x.rolling(4, min_periods=1).mean()
        )
        df["price_change_std_4w"] = df.groupby("county")["price_change"].transform(
            lambda x: x.rolling(4, min_periods=1).std()
        ).fillna(0)
        return df.dropna(subset=["price_change"]).reset_index(drop=True)

    def get_feature_cols(self, df):
        exclude = [
            "county", "week_start", "kamis_price", "kamis_std", "agri_price", "agri_std",
            "season", "price", "price_change"
        ]
        return [c for c in df.columns if c not in exclude and df[c].notna().sum() > 0]

    def build_pooled(self, X_train_df, y_train_arr):
        split = min(int(len(X_train_df) * 0.8), len(X_train_df) - 10)
        xgb = XGBRegressor(
            n_estimators=500, max_depth=3, learning_rate=0.05,
            reg_lambda=5, subsample=0.7, colsample_bytree=0.8,
            early_stopping_rounds=15, random_state=42, n_jobs=-1
        )
        xgb.fit(
            X_train_df.iloc[:split], y_train_arr[:split],
            eval_set=[(X_train_df.iloc[split:], y_train_arr[split:])],
            verbose=False
        )
        return xgb

    def evaluate(self, y_true_change, pred_change, y_true_price, pred_price,
                 y_train_change, county, model_name):
        m = mean_absolute_error(y_true_change, pred_change)
        mase_val = mase(y_true_change, pred_change, y_train_change)
        da = directional_accuracy(y_true_change, pred_change)
        mae_price = mean_absolute_error(y_true_price, pred_price)
        smape_val = smape(y_true_price, pred_price)
        return {
            "county": county, "model": model_name,
            "mae_change": m, "mase": mase_val, "dir_acc": da,
            "mae_price": mae_price, "smape": smape_val
        }

    def train_and_evaluate(self):
        panel = pd.read_csv(FEATURES_DIR / "panel_features.csv", parse_dates=["week_start"])
        df = self.prepare_data(panel)
        weeks = sorted(df['week_start'].unique())
        n_weeks = len(weeks)
        feat_cols = self.get_feature_cols(df)

        n_folds = 5
        initial_train_pct = 0.55
        initial_train = int(n_weeks * initial_train_pct)
        fold_size = max(8, (n_weeks - initial_train) // n_folds)

        all_results = []
        models = {}

        print(f"Weeks: {n_weeks}, Initial train: {initial_train}, Fold size: {fold_size}")
        print(f"Feature cols ({len(feat_cols)}): {feat_cols[:8]}...")
        print(f"{'='*70}")
        print(f"{'Fold':>5} {'Train':>8} {'Test':>8} {'County':>14} {'Model':>22} {'MASE':>7} {'Dir%':>7} {'MAE$':>8} {'sMAPE':>7}")
        print(f"{'='*70}")

        for fold in range(n_folds):
            train_end = initial_train + fold * fold_size
            test_start = train_end
            test_end = min(test_start + fold_size, n_weeks)
            if test_end - test_start < 4:
                break

            train_weeks = weeks[:train_end]
            test_weeks = weeks[test_start:test_end]
            train_df = df[df['week_start'].isin(train_weeks)].copy()
            test_df = df[df['week_start'].isin(test_weeks)].copy()

            if train_df.empty or test_df.empty:
                continue

            # --- Features with county dummies ---
            county_dummies = pd.get_dummies(train_df['county'], prefix='c')
            dummy_cols = county_dummies.columns

            X_tr = pd.concat([train_df[feat_cols].fillna(0), county_dummies], axis=1)
            y_tr_change = train_df['price_change'].values
            y_tr_price = train_df['price'].values
            y_tr_change_series = train_df['price_change']

            test_dummies = pd.get_dummies(test_df['county'], prefix='c').reindex(columns=dummy_cols, fill_value=0)
            X_te = pd.concat([test_df[feat_cols].fillna(0), test_dummies], axis=1)
            y_te_change = test_df['price_change'].values
            y_te_price = test_df['price'].values
            county_labels = test_df['county'].values

            # --- Pooled XGBoost ---
            pooled = self.build_pooled(X_tr, y_tr_change)
            if fold == 0:
                self.pooled_xgb = pooled

            pool_pred_change = pooled.predict(X_te)
            pool_pred_price = test_df['price'].values - test_df['price_change'].values + pool_pred_change

            for county in self.target_counties:
                mask = county_labels == county
                if mask.sum() < 3:
                    continue

                m = self.evaluate(
                    y_te_change[mask], pool_pred_change[mask],
                    y_te_price[mask], pool_pred_price[mask],
                    y_tr_change_series, county, "pooled_xgboost"
                )
                all_results.append(m)
                print(f"{fold:>5} {train_end:>8} {test_end:>8} {county:>14} {'pooled_xgboost':>22} {m['mase']:>7.3f} {m['dir_acc']:>7.1%} {m['mae_price']:>8.2f} {m['smape']:>7.2f}")

            # --- Fine-tuned per county ---
            for county in self.target_counties:
                c_train = train_df[train_df['county'] == county]
                c_test = test_df[test_df['county'] == county]
                if len(c_train) < 10 or len(c_test) < 3:
                    continue

                Xc_tr = pd.concat([c_train[feat_cols].fillna(0),
                                   pd.get_dummies(c_train['county'], prefix='c').reindex(columns=dummy_cols, fill_value=0)], axis=1)
                yc_tr_change = c_train['price_change'].values
                Xc_te = pd.concat([c_test[feat_cols].fillna(0),
                                   pd.get_dummies(c_test['county'], prefix='c').reindex(columns=dummy_cols, fill_value=0)], axis=1)

                ft = XGBRegressor(
                    n_estimators=150, max_depth=3, learning_rate=0.01,
                    reg_lambda=3, subsample=0.8, colsample_bytree=0.8,
                    random_state=42, n_jobs=-1
                )
                ft.fit(Xc_tr, yc_tr_change, xgb_model=pooled.get_booster(), verbose=False)

                ft_pred_change = ft.predict(Xc_te)
                ft_pred_price = c_test['price'].values - c_test['price_change'].values + ft_pred_change

                m = self.evaluate(
                    c_test['price_change'].values, ft_pred_change,
                    c_test['price'].values, ft_pred_price,
                    y_tr_change_series, county, "fine_tuned_xgboost"
                )
                all_results.append(m)
                print(f"{fold:>5} {train_end:>8} {test_end:>8} {county:>14} {'fine_tuned_xgboost':>22} {m['mase']:>7.3f} {m['dir_acc']:>7.1%} {m['mae_price']:>8.2f} {m['smape']:>7.2f}")

        # --- Persistence baseline (evaluate same way) ---
        print(f"\n{'='*70}")
        print("  PERSISTENCE BASELINE (all folds)")
        print(f"{'='*70}")
        for fold in range(n_folds):
            train_end = initial_train + fold * fold_size
            test_start = train_end
            test_end = min(test_start + fold_size, n_weeks)
            if test_end - test_start < 4:
                break
            test_weeks = weeks[test_start:test_end]
            test_df = df[df['week_start'].isin(test_weeks)].copy()

            for county in self.target_counties:
                cd = test_df[test_df['county'] == county].sort_values('week_start')
                if len(cd) < 3:
                    continue

                y_tc = cd['price_change'].values
                y_tp = cd['price'].values
                pred_change = np.zeros(len(y_tc))
                pred_price = cd['price'].values - y_tc + pred_change  # = previous price

                m = self.evaluate(y_tc, pred_change, y_tp, pred_price,
                                  y_tc, county, "persistence")
                all_results.append(m)
                print(f"{fold:>5} {train_end:>8} {test_end:>8} {county:>14} {'persistence':>22} {m['mase']:>7.3f} {m['dir_acc']:>7.1%} {m['mae_price']:>8.2f} {m['smape']:>7.2f}")

        # ===== SUMMARY =====
        results_df = pd.DataFrame(all_results)
        MODELS_DIR.mkdir(parents=True, exist_ok=True)
        results_df.to_csv(MODELS_DIR / "model_evaluation.csv", index=False)

        import joblib
        import json
        if self.pooled_xgb:
            joblib.dump(self.pooled_xgb, MODELS_DIR / "pooled_xgboost.pkl")

        config = {"feat_cols": list(feat_cols), "dummy_cols": list(dummy_cols)}
        json.dump(config, open(MODELS_DIR / "model_config.json", "w"), indent=2)

        print(f"\n{'='*70}")
        print("  AGGREGATE RESULTS")
        print(f"{'='*70}")
        for model in ["persistence", "pooled_xgboost", "fine_tuned_xgboost"]:
            sub = results_df[results_df["model"] == model]
            if sub.empty:
                continue
            print(f"\n  {model}:")
            print(f"    MASE:      {sub['mase'].mean():.3f}")
            print(f"    Dir Acc:   {sub['dir_acc'].mean():.1%}")
            print(f"    MAE (KES): {sub['mae_price'].mean():.2f}")
            print(f"    sMAPE:     {sub['smape'].mean():.2f}%")

        print(f"\n{'='*70}")
        print("  BEST MODEL PER COUNTY")
        print(f"{'='*70}")
        for c in self.target_counties:
            cr = results_df[results_df["county"] == c]
            if cr.empty:
                continue
            pivot = cr.groupby("model").agg({"mase": "mean", "dir_acc": "mean", "mae_price": "mean"}).reset_index()
            best = pivot.loc[pivot["mase"].idxmin()]
            print(f"  {c:>14}: {best['model']:>22}  MASE={best['mase']:.3f}  Dir={best['dir_acc']:.1%}  MAE={best['mae_price']:.2f}")

        return results_df


if __name__ == "__main__":
    MaizePriceForecaster().train_and_evaluate()
