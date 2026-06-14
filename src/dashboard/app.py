import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import json
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).parent.parent.parent
MODELS_DIR = BASE_DIR / "models"
FEATURES_DIR = BASE_DIR / "data" / "features"
FORECAST_WEEKS = 8

TARGET_COUNTIES = ["Kiambu", "Kirinyaga", "Mombasa", "Nairobi", "Uasin-Gishu"]

st.set_page_config(page_title="Maize Price Forecast", page_icon="🌽", layout="wide")


# ── Cached loads ──────────────────────────────────────────────────────────

@st.cache_data
def load_data():
    return pd.read_csv(FEATURES_DIR / "panel_features.csv", parse_dates=["week_start"])


@st.cache_resource
def load_model():
    return joblib.load(MODELS_DIR / "pooled_xgboost.pkl")


@st.cache_resource
def load_config():
    with open(MODELS_DIR / "model_config.json") as f:
        return json.load(f)


@st.cache_resource
def load_results():
    path = MODELS_DIR / "model_evaluation.csv"
    if path.exists():
        return pd.read_csv(path)
    return None


# ── Feature helpers ───────────────────────────────────────────────────────

def prepare_county_features(cd):
    df = cd.sort_values("week_start").copy()
    df["price_change"] = df["price"].diff(1)
    df["price_change_lag_1w"] = df["price_change"].shift(1)
    df["price_change_lag_2w"] = df["price_change"].shift(2)
    df["price_change_ma_4w"] = df["price_change"].rolling(4, min_periods=1).mean()
    df["price_change_std_4w"] = df["price_change"].rolling(4, min_periods=1).std().fillna(0)
    return df


def build_feature_row(df, idx, feat_cols):
    return df[feat_cols].fillna(0).iloc[idx]


def build_dummy_row(county, dummy_cols):
    row = pd.Series(0, index=dummy_cols)
    col = f"c_{county}"
    if col in dummy_cols:
        row[col] = 1
    return row


# ── Forecast engine ──────────────────────────────────────────────────────

def forecast_single_path(model, panel, county, config, n_weeks, noise_std=0):
    feat_cols, dummy_cols = config["feat_cols"], config["dummy_cols"]
    cd = panel[panel["county"] == county].sort_values("week_start").copy()
    last_date = cd["week_start"].max()
    sim = cd.tail(20).copy()
    sim = prepare_county_features(sim)

    for i in range(n_weeks):
        next_date = last_date + timedelta(weeks=i + 1)
        feats = build_feature_row(sim, len(sim) - 1, feat_cols)
        dummies = build_dummy_row(county, dummy_cols)
        X = pd.concat([feats, dummies]).to_frame().T
        X = X.reindex(columns=list(feat_cols) + list(dummy_cols), fill_value=0)

        raw = model.predict(X)[0]
        delta_pred = raw + np.random.normal(0, noise_std) if noise_std > 0 else raw
        last_price = sim["price"].iloc[-1]
        next_price = last_price + delta_pred

        new_row = sim.iloc[-1:].copy()
        new_row["week_start"] = next_date
        new_row["price"] = next_price
        for c in ["kamis_price", "kamis_std", "agri_price", "agri_std",
                   "temp_avg_c", "temp_max_c", "temp_min_c", "rain_mm",
                   "wind_speed_max_kmh", "usd_kes", "cpi", "inflation_rate",
                   "rain_sum_4w", "temp_avg_4w", "rain_sum_8w", "temp_avg_8w"]:
            if c in new_row.columns:
                new_row[c] = sim[c].iloc[-1]
        new_row["month"] = next_date.month
        new_row["week_of_year"] = next_date.isocalendar()[1]
        new_row["year"] = next_date.year
        new_row["days_from_start"] = sim["days_from_start"].iloc[-1] + 7
        new_row["season"] = "off_season"

        sim = pd.concat([sim, new_row], ignore_index=True)
        sim = prepare_county_features(sim)

    return sim["price"].iloc[-n_weeks:].values


def forecast_with_ci(model, panel, county, config, n_weeks, n_sims=200):
    best = forecast_single_path(model, panel, county, config, n_weeks, noise_std=0)
    paths = np.zeros((n_sims, n_weeks))
    for s in range(n_sims):
        paths[s] = forecast_single_path(model, panel, county, config, n_weeks, noise_std=0.8)
    lo = np.percentile(paths, 10, axis=0)
    hi = np.percentile(paths, 90, axis=0)
    return best, lo, hi


# ── Feature importance ────────────────────────────────────────────────────

def get_feature_importance(model, config):
    try:
        names = model.get_booster().feature_names
        scores = model.feature_importances_
        imp = pd.DataFrame({"feature": names, "importance": scores}).sort_values("importance", ascending=False)
        return imp.head(15)
    except Exception:
        return None


# ── Seasonal pattern ──────────────────────────────────────────────────────

def get_seasonal(panel, county):
    cd = panel[panel["county"] == county].dropna(subset=["price"]).copy()
    cd["month"] = pd.to_datetime(cd["week_start"]).dt.month
    seas = cd.groupby("month")["price"].agg(["mean", "std", "count"]).reset_index()
    seas.columns = ["month", "avg_price", "std_price", "n"]
    return seas


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    st.title("🌽 Maize Price Analysis")
    st.markdown("---")

    panel = load_data()
    model = load_model()
    config = load_config()
    results = load_results()
    feat_imp = get_feature_importance(model, config)

    col1, col2 = st.sidebar.columns(2)
    with col1:
        county = st.sidebar.selectbox("County", TARGET_COUNTIES)
    with col2:
        weeks = st.sidebar.slider("Forecast horizon", 4, 12, FORECAST_WEEKS)

    cd = panel[panel["county"] == county].sort_values("week_start").dropna(subset=["price"])

    def min_date():
        return cd["week_start"].min()
    def max_date():
        return cd["week_start"].max()
    def curr_price():
        return cd["price"].iloc[-1]
    def prev_price():
        return cd["price"].iloc[-2] if len(cd) >= 2 else curr_price()
    def chg_1w():
        return curr_price() - prev_price()

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🌦 Seasonality", "🔍 Drivers", "📈 Model Performance"])

    # ════════════════════════════════════════════════════════════════
    # TAB 1 — OVERVIEW
    # ════════════════════════════════════════════════════════════════
    with tab1:
        k1, k2, k3, k4 = st.columns(4)
        trend_4w = curr_price() - cd["price"].iloc[-5] if len(cd) >= 5 else 0
        k1.metric("Current Price", f"KES {curr_price():.0f}", f"{chg_1w():+.1f} / wk")
        k2.metric("4-Week Trend", f"{'▲' if trend_4w > 0 else '▼'}  KES {abs(trend_4w):.1f}", f"{trend_4w / 4:+.1f} avg/wk")
        k3.metric("Date Range", f"{min_date().strftime('%b %Y')} – {max_date().strftime('%b %Y')}")
        k4.metric("Volatility (σ)", f"KES {cd['price'].std():.1f}")

        with st.spinner("Generating forecast..."):
            best_path, ci_lo, ci_hi = forecast_with_ci(model, panel, county, config, weeks)

        fc_dates = [max_date() + timedelta(weeks=i + 1) for i in range(weeks)]

        fig, ax = plt.subplots(figsize=(14, 5))
        ax.plot(cd["week_start"], cd["price"], color="#2563eb", linewidth=1.2, label="Historical")
        ax.fill_between(cd["week_start"], cd["price"], alpha=0.06, color="#2563eb")

        ax.fill_between(fc_dates, ci_lo, ci_hi, color="#dc2626", alpha=0.18, label="50–90% CI")
        ax.plot(fc_dates, best_path, color="#dc2626", linewidth=2, linestyle="--", marker="o", label="Forecast (median)")

        bridge_x = [max_date(), fc_dates[0]]
        bridge_y = [curr_price(), best_path[0]]
        ax.plot(bridge_x, bridge_y, color="#dc2626", linewidth=1, linestyle=":")

        ax.axhline(y=curr_price(), color="#dc2626", linewidth=0.7, linestyle=":", alpha=0.3)
        ax.set_ylabel("Price (KES)")
        ax.legend(frameon=True, fancybox=True, loc="upper left")
        ax.grid(True, alpha=0.15)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        fc_df = pd.DataFrame({
            "Week": [d.strftime("%Y-%m-%d") for d in fc_dates],
            "Forecast (KES)": best_path.round(1),
            "Δ": np.diff([curr_price()] + list(best_path)).round(2),
            "CI Low (KES)": ci_lo.round(1),
            "CI High (KES)": ci_hi.round(1),
        })
        st.dataframe(fc_df, hide_index=True, use_container_width=True)

    # ════════════════════════════════════════════════════════════════
    # TAB 2 — SEASONALITY  (Descriptive)
    # ════════════════════════════════════════════════════════════════
    with tab2:
        seas = get_seasonal(panel, county)
        all_months = pd.DataFrame({"month": range(1, 13)})
        seas = all_months.merge(seas, on="month", how="left").fillna(0)
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4.5))

        # Monthly average bar
        colors = ["#2563eb"] * 12
        ax1.bar(month_names, seas["avg_price"], color=colors, edgecolor="white", linewidth=0.5)
        ax1.set_ylabel("Avg Price (KES)")
        ax1.set_title(f"{county} — Monthly Average Price")
        ax1.grid(axis="y", alpha=0.2)
        for i, (_, r) in enumerate(seas.iterrows()):
            ax1.text(i, r["avg_price"] + 0.5, f"{r['avg_price']:.0f}", ha="center", fontsize=8)

        # Year-over-year (if multiple years)
        cd2 = panel[panel["county"] == county].dropna(subset=["price"]).copy()
        cd2["year"] = pd.to_datetime(cd2["week_start"]).dt.year
        years = sorted(cd2["year"].unique())
        if len(years) > 1:
            for yr in years:
                yy = cd2[cd2["year"] == yr].copy()
                yy["week_of_year"] = pd.to_datetime(yy["week_start"]).dt.isocalendar().week.astype(int)
                yy = yy.sort_values("week_of_year")
                ax2.plot(yy["week_of_year"], yy["price"], label=str(yr), linewidth=1.2)
            ax2.set_xlabel("Week of Year")
            ax2.set_ylabel("Price (KES)")
            ax2.set_title("Year-over-Year Comparison")
            ax2.legend(frameon=True, fancybox=True)
            ax2.grid(True, alpha=0.15)
        else:
            ax2.text(0.5, 0.5, "Only one year of data", ha="center", va="center", transform=ax2.transAxes, fontsize=12)
            ax2.set_title("Year-over-Year Comparison")

        plt.tight_layout()
        st.pyplot(fig2)

        with st.expander("Descriptive Statistics"):
            desc = cd["price"].describe().round(2).to_frame().T
            desc.index = [county]
            st.dataframe(desc, use_container_width=True)

    # ════════════════════════════════════════════════════════════════
    # TAB 3 — DRIVERS  (Diagnostic)
    # ════════════════════════════════════════════════════════════════
    with tab3:
        col_d1, col_d2 = st.columns([1, 1])

        with col_d1:
            st.subheader("Feature Importance (Top 15)")
            if feat_imp is not None:
                fig3, ax3 = plt.subplots(figsize=(7, 5))
                top15 = feat_imp.head(15)
                imp_vals = top15["importance"].values
                feat_names = [n[:28] + "…" if len(n) > 30 else n for n in top15["feature"]]
                ax3.barh(range(len(imp_vals)), imp_vals, color="#2563eb", edgecolor="white")
                ax3.set_yticks(range(len(imp_vals)))
                ax3.set_yticklabels(feat_names, fontsize=8)
                ax3.invert_yaxis()
                ax3.set_xlabel("Importance")
                ax3.set_title("What drives maize prices?")
                ax3.grid(axis="x", alpha=0.2)
                plt.tight_layout()
                st.pyplot(fig3)
            else:
                st.warning("Feature importance not available")

        with col_d2:
            st.subheader("Current Feature Values")
            last_row = cd.iloc[-1]
            driver_cols = [c for c in ["cpi", "usd_kes", "inflation_rate",
                                         "temp_avg_c", "rain_mm",
                                         "price_lag_1w", "price_ma_4w"]
                           if c in cd.columns]
            drivers = last_row[driver_cols].to_frame().reset_index()
            drivers.columns = ["Feature", "Current Value"]
            drivers["Current Value"] = drivers["Current Value"].round(2)
            st.dataframe(drivers, hide_index=True, use_container_width=True)

        st.subheader("How key drivers relate to price")
        driver_plot_cols = [c for c in ["cpi", "usd_kes", "inflation_rate", "temp_avg_c", "rain_mm"]
                            if c in cd.columns]
        n_drivers = len(driver_plot_cols)
        if n_drivers > 0:
            fig4, axes = plt.subplots(1, n_drivers, figsize=(4 * n_drivers, 3.5))
            if n_drivers == 1:
                axes = [axes]
            for ax4, col in zip(axes, driver_plot_cols):
                ax4.scatter(cd[col], cd["price"], alpha=0.5, s=15, color="#2563eb")
                z = np.polyfit(cd[col].fillna(0), cd["price"].fillna(0), 1)
                p = np.poly1d(z)
                xv = np.linspace(cd[col].min(), cd[col].max(), 50)
                ax4.plot(xv, p(xv), color="#dc2626", linewidth=1, linestyle="--")
                ax4.set_xlabel(col)
                ax4.set_ylabel("Price (KES)")
                ax4.grid(True, alpha=0.15)
            plt.tight_layout()
            st.pyplot(fig4)

    # ════════════════════════════════════════════════════════════════
    # TAB 4 — MODEL PERFORMANCE  (Diagnostic)
    # ════════════════════════════════════════════════════════════════
    with tab4:
        st.subheader("Per-County Model Performance")
        if results is not None:
            pivot = results.groupby(["county", "model"]).agg(
                MASE=("mase", "mean"),
                Dir_Acc=("dir_acc", "mean"),
                MAE_KES=("mae_price", "mean"),
                sMAPE=("smape", "mean")
            ).round(3).reset_index()
            st.dataframe(pivot, hide_index=True, use_container_width=True)

            st.subheader("Best Model per County")
            best = pivot.loc[pivot.groupby("county")["MASE"].idxmin()].reset_index(drop=True)
            st.dataframe(best, hide_index=True, use_container_width=True)
        else:
            st.warning("No evaluation results found — run train.py first")

        if results is not None:
            st.subheader(f"Performance Summary — {county}")
            cr = results[results["county"] == county]
            if not cr.empty:
                fig5, axes = plt.subplots(1, 3, figsize=(14, 3.5))
                models_ = cr["model"].unique()
                x = np.arange(len(models_))
                width = 0.25
                for ax5, metric, title, color in zip(
                    axes, ["mase", "dir_acc", "mae_price"],
                    ["MASE ↓", "Directional Accuracy ↑", "MAE (KES) ↓"],
                    ["#2563eb", "#16a34a", "#dc2626"]
                ):
                    vals = [cr[cr["model"] == m][metric].mean() for m in models_]
                    ax5.bar(x, vals, width, color=color, alpha=0.8, edgecolor="white")
                    ax5.set_xticks(x)
                    ax5.set_xticklabels([m[:12] + "…" if len(m) > 14 else m for m in models_], fontsize=8)
                    ax5.set_title(title)
                    ax5.grid(axis="y", alpha=0.2)
                plt.tight_layout()
                st.pyplot(fig5)

    st.caption(f"Data: KAMIS / AgriBORA · Model: XGBoost on Δ-price · {weeks}-week horizon · CI from {200} simulations")


if __name__ == "__main__":
    main()
