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

st.set_page_config(page_title="Maize Price Guide - Kenya", page_icon="🌽", layout="wide")


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


# ── Forecast engine (unchanged) ───────────────────────────────────────────

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


def forecast_with_ci(model, panel, county, config, n_weeks, noise_std=0.8, z=1.28):
    best = forecast_single_path(model, panel, county, config, n_weeks, noise_std=0)
    ci_band = noise_std * z * np.sqrt(np.arange(1, n_weeks + 1))
    lo = best - ci_band
    hi = best + ci_band
    return best, lo, hi


# ── Plain-language helpers ────────────────────────────────────────────────

def price_signal(current_price, forecast, lo, hi):
    avg_fc = np.mean(forecast)
    pct_change = (avg_fc - current_price) / current_price * 100
    if pct_change > 3:
        return "📈 Rising", f"Prices expected to rise about {pct_change:.0f}% — good time to sell if you're a farmer, buy now if you're a consumer", "#dc2626"
    elif pct_change < -3:
        return "📉 Falling", f"Prices expected to drop about {abs(pct_change):.0f}% — wait if buying, sell now if you're a farmer", "#16a34a"
    else:
        return "➡️ Stable", f"Prices expected to stay steady (within {abs(pct_change):.0f}%) — no urgent action needed", "#2563eb"


def best_time_advice(seas):
    if seas.empty:
        return "Not enough data"
    peak = seas.loc[seas["avg_price"].idxmax()]
    trough = seas.loc[seas["avg_price"].idxmin()]
    month_names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return {
        "best_sell_month": month_names[int(peak["month"])],
        "best_sell_price": f"KES {peak['avg_price']:.0f}",
        "best_buy_month": month_names[int(trough["month"])],
        "best_buy_price": f"KES {trough['avg_price']:.0f}",
        "peak_month": month_names[int(peak["month"])],
        "trough_month": month_names[int(trough["month"])],
    }


def county_ranking(panel, forecast_results):
    rows = []
    for c in TARGET_COUNTIES:
        cd = panel[panel["county"] == c].dropna(subset=["price"])
        if cd.empty:
            continue
        curr = cd["price"].iloc[-1]
        fc = forecast_results.get(c)
        if fc is not None:
            best_path = fc[0]
            fc_change = best_path[-1] - curr
            rows.append({"County": c, "Current Price": f"KES {curr:.0f}",
                         "Forecast Trend": "Rising" if fc_change > 0 else "Falling" if fc_change < 0 else "Stable",
                         "Price (forecast)": f"KES {best_path[-1]:.0f}"})
        else:
            rows.append({"County": c, "Current Price": f"KES {curr:.0f}",
                         "Forecast Trend": "—", "Price (forecast)": "—"})
    return pd.DataFrame(rows)


def seasonal_chart_advice(seas):
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    now = pd.Timestamp.now().month
    current_avg = seas.loc[seas["month"] == now, "avg_price"].values
    current_avg = current_avg[0] if len(current_avg) > 0 else None
    text_parts = []
    for i, row in seas.iterrows():
        m = int(row["month"])
        label = month_names[m - 1]
        emoji = "🔴" if row["avg_price"] > seas["avg_price"].mean() else "🟢"
        text_parts.append(f"{emoji} **{label}**: KES {row['avg_price']:.0f}")
    return text_parts


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    st.title("🌽 Maize Price Guide for Kenya")
    st.markdown("_Simple price forecasts to help farmers, traders, and families plan ahead_")

    panel = load_data()
    model = load_model()
    config = load_config()

    col1, col2 = st.sidebar.columns(2)
    with col1:
        county = st.sidebar.selectbox("Your County", TARGET_COUNTIES)
    with col2:
        weeks = st.sidebar.slider("Look ahead (weeks)", 4, 12, FORECAST_WEEKS)

    cd = panel[panel["county"] == county].sort_values("week_start").dropna(subset=["price"])
    if cd.empty:
        st.error(f"No data available for {county}")
        return

    # Compute seasonal patterns once
    def get_seasonal():
        cd2 = panel[panel["county"] == county].dropna(subset=["price"]).copy()
        cd2["month"] = pd.to_datetime(cd2["week_start"]).dt.month
        seas = cd2.groupby("month")["price"].agg(["mean", "std", "count"]).reset_index()
        seas.columns = ["month", "avg_price", "std_price", "n"]
        all_months = pd.DataFrame({"month": range(1, 13)})
        seas = all_months.merge(seas, on="month", how="left").fillna(0)
        return seas

    seas = get_seasonal()

    # ── Sidebar KPI cards ──────────────────────────────────────────────────
    curr_price = cd["price"].iloc[-1]
    prev_price = cd["price"].iloc[-2] if len(cd) >= 2 else curr_price
    chg_1w = curr_price - prev_price
    trend_4w = curr_price - cd["price"].iloc[-5] if len(cd) >= 5 else 0
    price_min = cd["price"].min()
    price_max = cd["price"].max()

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### {county} Now")
    st.sidebar.metric("Current Price", f"KES {curr_price:.0f}", f"{chg_1w:+.1f} / wk")
    st.sidebar.metric("4-Week Trend", f"{'▲' if trend_4w > 0 else '▼'} KES {abs(trend_4w):.1f}")
    st.sidebar.metric("Range (all time)", f"KES {price_min:.0f} – KES {price_max:.0f}")

    # Generate forecasts for all counties (for market comparison)
    @st.cache_data(ttl=300)
    def get_all_forecasts(weeks):
        results = {}
        for c in TARGET_COUNTIES:
            cdata = panel[panel["county"] == c].dropna(subset=["price"])
            if len(cdata) < 10:
                continue
            try:
                results[c] = forecast_with_ci(model, panel, c, config, weeks)
            except Exception:
                pass
        return results

    with st.spinner("Generating forecasts across all markets..."):
        all_fc = get_all_forecasts(weeks)

    # My county forecast
    my_fc = all_fc.get(county)
    if my_fc is None:
        st.warning("Could not generate forecast for this county")
        return

    best_path, ci_lo, ci_hi = my_fc
    max_date = cd["week_start"].max()
    fc_dates = [max_date + timedelta(weeks=i + 1) for i in range(weeks)]
    signal_text, signal_desc, signal_color = price_signal(curr_price, best_path, ci_lo, ci_hi)

    # ══════════════════════════════════════════════════════════════════════
    tab1, tab2, tab3 = st.tabs(["📈 Price Forecast", "🏪 Compare Markets", "🗓 Best Time & Tips"])

    # ══════════════════════════════════════════════════════════════════════
    # TAB 1 — PRICE FORECAST (user-friendly)
    # ══════════════════════════════════════════════════════════════════════
    with tab1:
        st.markdown(f"## Price outlook for **{county}**")

        # Signal banner
        st.markdown(
            f"<div style='padding:1rem;border-radius:8px;background:{signal_color}15;"
            f"border-left:5px solid {signal_color}'>"
            f"<h3 style='margin:0;color:{signal_color}'>{signal_text}</h3>"
            f"<p style='margin:0.5rem 0 0 0;font-size:1.05rem'>{signal_desc}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )

        # Forecast chart
        fig, ax = plt.subplots(figsize=(14, 5))
        ax.plot(cd["week_start"], cd["price"], color="#2563eb", linewidth=1.5, label="Past prices")
        ax.fill_between(cd["week_start"], cd["price"], alpha=0.06, color="#2563eb")
        ax.fill_between(fc_dates, ci_lo, ci_hi, color="#dc2626", alpha=0.18, label="Possible range")
        ax.plot(fc_dates, best_path, color="#dc2626", linewidth=2.5, linestyle="--", marker="o", label="Forecast")
        bridge_x = [max_date, fc_dates[0]]
        bridge_y = [curr_price, best_path[0]]
        ax.plot(bridge_x, bridge_y, color="#dc2626", linewidth=1, linestyle=":")

        ax.axhline(y=curr_price, color="#dc2626", linewidth=0.7, linestyle=":", alpha=0.3)
        ax.set_ylabel("Price (KES)")
        ax.set_title(f"Maize price forecast — {county}")
        ax.legend(frameon=True, fancybox=True, loc="upper left")
        ax.grid(True, alpha=0.15)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Simple forecast table
        fc_df = pd.DataFrame({
            "Week ending": [d.strftime("%d %b %Y") for d in fc_dates],
            "Expected Price": [f"KES {p:.0f}" for p in best_path],
            "Change from now": [f"{'▲' if d > 0 else '▼'} KES {abs(d):.1f}" if abs(d) > 0.1 else "—" for d in np.diff([curr_price] + list(best_path))],
            "Possible low": [f"KES {l:.0f}" for l in ci_lo],
            "Possible high": [f"KES {h:.0f}" for h in ci_hi],
        })
        st.dataframe(fc_df, hide_index=True, use_container_width=True)

        st.caption(f"The 'Possible range' column shows what prices could be in 9 out of 10 scenarios. "
                   f"Based on past data and current market conditions in {county}.")

    # ══════════════════════════════════════════════════════════════════════
    # TAB 2 — MARKET COMPARISON (for farmers deciding where to sell/buy)
    # ══════════════════════════════════════════════════════════════════════
    with tab2:
        st.markdown("## Compare prices across Kenyan markets")

        rank_df = county_ranking(panel, all_fc)
        st.markdown("### Current Prices by County")
        st.dataframe(rank_df, hide_index=True, use_container_width=True)

        # Highlight best/worst
        current_prices = {}
        for c in TARGET_COUNTIES:
            cdata = panel[panel["county"] == c].dropna(subset=["price"])
            if not cdata.empty:
                current_prices[c] = cdata["price"].iloc[-1]

        if current_prices:
            best_sell = max(current_prices, key=current_prices.get)
            best_buy = min(current_prices, key=current_prices.get)
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(
                    f"<div style='padding:1rem;border-radius:8px;background:#16a34a15;"
                    f"border-left:5px solid #16a34a'>"
                    f"<h4 style='margin:0;color:#16a34a'>🏪 Best market to SELL</h4>"
                    f"<p style='margin:0.3rem 0 0 0;font-size:1.2rem'><b>{best_sell}</b> — "
                    f"KES {current_prices[best_sell]:.0f} per kg</p>"
                    f"<p style='margin:0.2rem 0 0 0;font-size:0.9rem'>Highest price right now</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
            with col_b:
                st.markdown(
                    f"<div style='padding:1rem;border-radius:8px;background:#2563eb15;"
                    f"border-left:5px solid #2563eb'>"
                    f"<h4 style='margin:0;color:#2563eb'>🛒 Best market to BUY</h4>"
                    f"<p style='margin:0.3rem 0 0 0;font-size:1.2rem'><b>{best_buy}</b> — "
                    f"KES {current_prices[best_buy]:.0f} per kg</p>"
                    f"<p style='margin:0.2rem 0 0 0;font-size:0.9rem'>Lowest price right now</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

        # Multi-county forecast comparison chart
        st.markdown("### Price forecast across all counties")
        fig2, ax2 = plt.subplots(figsize=(14, 5))
        colors = ["#2563eb", "#16a34a", "#dc2626", "#f59e0b", "#8b5cf6"]
        for idx, c in enumerate(TARGET_COUNTIES):
            fc = all_fc.get(c)
            if fc is None:
                continue
            best, _, _ = fc
            cdata = panel[panel["county"] == c].dropna(subset=["price"])
            if cdata.empty:
                continue
            last_date = cdata["week_start"].max()
            fc_dates_c = [last_date + timedelta(weeks=i + 1) for i in range(weeks)]
            bridge_x = [last_date, fc_dates_c[0]]
            bridge_y = [cdata["price"].iloc[-1], best[0]]
            ax2.plot(fc_dates_c, best, color=colors[idx % len(colors)], linewidth=2, marker="o", label=c)
            ax2.plot(bridge_x, bridge_y, color=colors[idx % len(colors)], linewidth=1, linestyle=":")
        ax2.set_ylabel("Price (KES)")
        ax2.set_title("Forecast comparison across counties")
        ax2.legend(frameon=True, fancybox=True, loc="best")
        ax2.grid(True, alpha=0.15)
        plt.xticks(rotation=45)
        st.pyplot(fig2)

    # ══════════════════════════════════════════════════════════════════════
    # TAB 3 — SEASONALITY + TIPS (plain language)
    # ══════════════════════════════════════════════════════════════════════
    with tab3:
        st.markdown(f"## Best time to buy or sell in **{county}**")

        advice = best_time_advice(seas)

        if advice:
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                st.markdown(
                    f"<div style='padding:1rem;border-radius:8px;background:#16a34a15;"
                    f"border-left:5px solid #16a34a;text-align:center'>"
                    f"<h4 style='margin:0;color:#16a34a'>🌾 Best month to SELL</h4>"
                    f"<p style='margin:0.3rem 0 0 0;font-size:2rem'><b>{advice['best_sell_month']}</b></p>"
                    f"<p style='margin:0;font-size:1.1rem'>Avg price: {advice['best_sell_price']}</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
            with col_s2:
                st.markdown(
                    f"<div style='padding:1rem;border-radius:8px;background:#2563eb15;"
                    f"border-left:5px solid #2563eb;text-align:center'>"
                    f"<h4 style='margin:0;color:#2563eb'>🛒 Best month to BUY</h4>"
                    f"<p style='margin:0.3rem 0 0 0;font-size:2rem'><b>{advice['best_buy_month']}</b></p>"
                    f"<p style='margin:0;font-size:1.1rem'>Avg price: {advice['best_buy_price']}</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

        # Monthly price chart
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_emojis = seasonal_chart_advice(seas)
        mean_price = seas["avg_price"].mean()

        fig3, ax3 = plt.subplots(figsize=(12, 4))
        bar_colors = ["#16a34a" if r["avg_price"] <= mean_price else "#dc2626" for _, r in seas.iterrows()]
        ax3.bar(month_names, seas["avg_price"], color=bar_colors, edgecolor="white", linewidth=0.5)
        ax3.axhline(y=mean_price, color="#2563eb", linewidth=1, linestyle="--", label=f"Average: KES {mean_price:.0f}")
        ax3.set_ylabel("Avg Price (KES)")
        ax3.set_title(f"{county} — Monthly average maize price")
        ax3.legend()
        ax3.grid(axis="y", alpha=0.2)
        for i, (_, r) in enumerate(seas.iterrows()):
            ax3.text(i, r["avg_price"] + 0.3, f"{r['avg_price']:.0f}", ha="center", fontsize=9)
        st.pyplot(fig3)

        with st.expander("📅 Month-by-month price guide"):
            st.markdown(f"**Average price: KES {mean_price:.0f}**")
            st.markdown("🟢 Green = below average (cheaper to buy)")
            st.markdown("🔴 Red = above average (better to sell)")
            for line in month_emojis:
                st.markdown(line)

        # Year-over-year
        cd2 = panel[panel["county"] == county].dropna(subset=["price"]).copy()
        cd2["year"] = pd.to_datetime(cd2["week_start"]).dt.year
        years = sorted(cd2["year"].unique())
        if len(years) > 1:
            st.markdown("### Year-over-year comparison")
            fig4, ax4 = plt.subplots(figsize=(12, 4))
            for yr in years:
                yy = cd2[cd2["year"] == yr].copy()
                yy["week_of_year"] = pd.to_datetime(yy["week_start"]).dt.isocalendar().week.astype(int)
                yy = yy.sort_values("week_of_year")
                ax4.plot(yy["week_of_year"], yy["price"], label=str(yr), linewidth=1.5)
            ax4.set_xlabel("Week of Year")
            ax4.set_ylabel("Price (KES)")
            ax4.set_title(f"{county} — Price trend by year")
            ax4.legend(frameon=True, fancybox=True)
            ax4.grid(True, alpha=0.15)
            st.pyplot(fig4)

        # ── Tips section ──
        st.markdown("---")
        st.markdown("## 💡 Tips for farmers & buyers")

        def trend_direction():
            chg = best_path[-1] - curr_price
            if chg > curr_price * 0.03:
                return "rising", "sell", "buy now before prices go higher"
            elif chg < -curr_price * 0.03:
                return "falling", "wait for prices to stabilize", "wait — prices may drop further"
            else:
                return "stable", "your call — prices are steady", "no rush — prices are steady"

        trend, farmer_advice, buyer_advice = trend_direction()

        trend_bg   = {'rising':'#16a34a','falling':'#dc2626','stable':'#d97706'}
        trend_icon = {'rising':'🚀','falling':'🔻','stable':'➡️'}
        trend_txt  = {'rising':'RISING ↑','falling':'FALLING ↓','stable':'STABLE →'}

        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown(
                f"<div style='padding:1.2rem;border-radius:10px;background:#fff7ed;"
                f"border:2px solid #ea580c;height:150px'>"
                f"<h4 style='margin:0;color:#c2410c;font-size:1.1rem'>🌾 For Farmers</h4>"
                f"<p style='margin:0.5rem 0 0 0;color:#000;font-size:1rem;font-weight:700'>"
                f"Prices are <span style='background:{trend_bg[trend]};color:#fff;"
                f"padding:0.1rem 0.5rem;border-radius:4px;font-size:1.1rem'>{trend_icon[trend]} {trend_txt[trend]}</span> "
                f"in <b>{county}</b>.</p>"
                f"<p style='margin:0.4rem 0 0 0;color:#9a3412;font-size:1.05rem;font-weight:800'>"
                f"👉 <u>{farmer_advice.capitalize()}.</u></p>"
                f"<p style='margin:0.4rem 0 0 0;color:#000;font-size:0.9rem'>"
                f"{'📈 Prices trending up — waiting a few weeks may get you better prices' if trend == 'rising' else '📉 Prices trending down — sell sooner rather than later' if trend == 'falling' else '➡️ No strong trend — sell when convenient'}"
                f"</p></div>",
                unsafe_allow_html=True,
            )
        with col_t2:
            st.markdown(
                f"<div style='padding:1.2rem;border-radius:10px;background:#eff6ff;"
                f"border:2px solid #2563eb;height:150px'>"
                f"<h4 style='margin:0;color:#1d4ed8;font-size:1.1rem'>🛒 For Families & Buyers</h4>"
                f"<p style='margin:0.5rem 0 0 0;color:#000;font-size:1rem;font-weight:700'>"
                f"In <b>{county}</b>, "
                f"<span style='background:{trend_bg[trend]};color:#fff;"
                f"padding:0.1rem 0.5rem;border-radius:4px;font-size:1.05rem'>👉 {buyer_advice}.</span></p>"
                f"<p style='margin:0.4rem 0 0 0;color:#000;font-size:0.9rem'>"
                f"{'📈 Prices rising — buy now before they go higher' if trend == 'rising' else '📉 Prices falling — waiting may get you a better deal' if trend == 'falling' else '➡️ Prices stable — buy when you need'}"
                f"</p></div>",
                unsafe_allow_html=True,
            )

        with st.expander("🔍 What drives maize prices? (simple explanation)"):
            st.markdown("""
            - **📊 Price momentum**: If prices rose last week, they tend to keep rising — this is the #1 predictor
            - **🌧 Weather**: Heavy rains reduce supply, which pushes prices up
            - **💰 Exchange rate**: When the Kenyan shilling weakens, imported food costs more
            - **📈 Inflation**: General price increases affect maize too
            - **🌾 Seasons**: Prices are lowest after harvests (Feb–Mar & Oct–Nov), highest during dry season (Jun–Jul)

            The model uses all these factors together to make its predictions.
            """)

    # Footer
    st.markdown("---")
    st.caption(f"Data: KAMIS & AgriBORA · Powered by machine learning · "
               f"Forecasts updated with latest available data · "
               f"Past performance does not guarantee future results")


if __name__ == "__main__":
    main()
