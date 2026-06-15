# 🌽 Maize Price Forecasting

End-to-end machine learning pipeline for forecasting maize prices across Kenyan counties. Uses a pooled XGBoost model on price changes (Δ-price) trained with expanding window cross-validation, with per-county fine-tuning. Deployable via Streamlit Cloud.

---

## Quick Start

```bash
pip install -r requirements.txt
python run.py                  # full pipeline: clean → features → train
streamlit run src/dashboard/app.py   # launch dashboard
```

Or deploy on [Streamlit Cloud](https://streamlit.io/cloud) — point to `streamlit_app.py` (auto-imports the dashboard).

---

## Project Structure

```
maize-forecasting/
├── data/
│   ├── raw/                  # Original datasets (not committed)
│   ├── processed/            # Cleaned datasets (not committed)
│   └── features/             # panel_features.csv (committed)
├── src/
│   ├── data/
│   │   ├── clean.py          # Clean KAMIS, AgriBORA, weather data
│   │   └── features.py       # Engineered features (lags, rolling stats, seasonals)
│   ├── models/
│   │   └── train.py          # Pooled XGBoost with expanding CV + fine-tuning
│   └── dashboard/
│       └── app.py            # Streamlit dashboard with 4 analysis tabs
├── models/                   # Trained .pkl + config + evaluation CSV
├── notebooks/                # Step-by-step pipeline notebook
├── streamlit_app.py          # Root entry point for Streamlit Cloud
├── run.py                    # Pipeline runner
├── requirements.txt          # Python dependencies
└── .gitignore
```

---

## Datasets

| Source | Description | Coverage |
|--------|-------------|----------|
| **KAMIS** | Kenya Agricultural Market Information System — retail/wholesale prices | 2021–2025, 46 counties |
| **AgriBORA** | Transaction-based wholesale maize prices | 2021–2025 |
| **Weather** | Daily temperature, rainfall (Open-Meteo) | 2021–2025, all counties |
| **Economic** | CPI, USD/KES exchange rate, inflation rate | 2021–2025 |

---

## Modeling Approach

### Core Strategy

1. **Target**: Δ-price (week-over-week change) — removes autocorrelation, makes persistence baseline predict zero
2. **Pooled XGBoost**: Single model trained on all 46 counties simultaneously using county one-hot encoding — allows information sharing across markets
3. **Expanding Window CV**: 5 folds, each fold adds 20 more weeks of training data — robust evaluation across time
4. **Fine-tuning**: Per-county XGBoost warm-started from the pooled model (optional, pooled model already captures county patterns via dummies)

### Features (30+)

- **Price lags**: 1, 2, 4, 8, 12 weeks
- **Δ-price features**: lags + rolling mean/std (4-week window)
- **Rolling statistics**: 4-, 8-, 12-week MA and std
- **Weather**: temperature (mean/max/min), rainfall, wind, 4/8-week aggregates
- **Economic**: CPI, USD/KES exchange rate, inflation rate
- **Temporal**: month, week_of_year, year, days_from_start
- **County dummies**: 46 one-hot encoded county indicators

### Metrics

| Metric | Interpretation |
|--------|---------------|
| **MASE** | Mean Absolute Scaled Error — compares to persistence (< 1 = beats "no change") |
| **Dir Acc** | Directional accuracy — % of weeks where up/down is correctly predicted |
| **MAE (KES)** | Mean Absolute Error on the original price scale |
| **sMAPE** | Symmetric Mean Absolute Percentage Error |

### Results (across 5 folds)

| Model | MASE | Dir Acc | MAE (KES) | sMAPE |
|-------|:---:|:-------:|:---------:|:-----:|
| Persistence | 0.63 | 0% | 2.89 | 7.15% |
| **Pooled XGBoost** | **0.32** | **76%** | **2.07** | **5.10%** |

MASE < 1 for all models — ML consistently beats persistence.

---

## Dashboard

The Streamlit dashboard has 4 tabs:

| Tab | Type | Content |
|-----|------|---------|
| **📊 Overview** | Predictive | Price history + 4–12 week forecast with 50–90% confidence bands, forecast table with Δ |
| **🌦 Seasonality** | Descriptive | Monthly average prices, year-over-year comparison, descriptive statistics |
| **🔍 Drivers** | Diagnostic | Top 15 feature importance, current feature values, scatter plots (CPI/USD/weather vs price) |
| **📈 Performance** | Diagnostic | MASE/Dir Acc/MAE/sMAPE per model per county, best-model-per-county table, bar charts |

---

## Target Counties

Kiambu · Kirinyaga · Mombasa · Nairobi · Uasin-Gishu

The pooled model was trained on all 46 counties; the dashboard shows the 5 most data-rich.

---

## Deployment

```bash
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/maize-forecasting.git
git push -u origin main
```

Then on [streamlit.io/cloud](https://streamlit.io/cloud): **New app** → select repo → main file path = `streamlit_app.py` → **Deploy**.

---

## Pipeline Runner

```bash
python run.py
```

Runs sequentially: `clean.py` → `features.py` → `train.py` → prints summary.

---

## Key Files

| File | Purpose |
|------|---------|
| `src/models/train.py` | Full training pipeline: Δ-price, pooled XGBoost, 5-fold expanding CV, per-county fine-tuning |
| `src/dashboard/app.py` | Streamlit app with 4-tab analysis dashboard |
| `streamlit_app.py` | Root entry point for Streamlit Cloud |
| `src/data/features.py` | Feature engineering: lags, rolling stats, seasonal flags |
| `notebooks/pipeline_step_by_step.ipynb` | Complete walkthrough notebook |
