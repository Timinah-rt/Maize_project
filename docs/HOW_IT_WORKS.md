# Maize Price Forecasting System — How It Works

## Overview

A machine learning system that predicts weekly maize prices for 5 Kenyan counties (Nairobi, Mombasa, Kiambu, Kirinyaga, Uasin-Gishu) up to 30 weeks into the future. Results are shown in an easy-to-use web dashboard.

---

## 1. Data Pipeline (raw data → ready-to-use dataset)

### Data Sources (5 sources)

| Source | What it provides |
|--------|------------------|
| **KAMIS** (Ministry of Agriculture) | Weekly retail & wholesale maize prices for each county |
| **AgriBORA** | Transaction-based wholesale prices (supplementary) |
| **Open-Meteo API** | Daily weather: temperature (mean/max/min), rainfall, wind speed |
| **KNBS** (Kenya National Bureau of Stats) | Monthly Consumer Price Index (CPI) |
| **Central Bank of Kenya** | Weekly USD/KES exchange rate |

### Cleaning (`src/data/clean.py`)
- Filters only white maize records
- Standardizes county names (so "Nairobi" and "Nairobi City" match)
- Removes extreme outliers (prices below KES 10 or above KES 200)
- Fills missing values forward (uses last known value)
- Clips unrealistic weather values

### Feature Engineering (`src/data/features.py`)
Combines all data sources into one table with **29 columns × 709 rows**. Key features:

**Price features:** Past prices (lagged 1–12 weeks), rolling average & standard deviation over 4/8/12 weeks

**Weather features:** Weekly mean/max/min temperature, total rainfall, max wind speed, rolling aggregates

**Economic features:** CPI, USD/KES exchange rate, inflation rate

**Time features:** Month, week of year, year, days from start of dataset

**County dummies:** 5 binary flags (one per county) so the model knows which county each row belongs to

### Output: `data/features/panel_features.csv`
- **709 rows** (5 counties × ~142 weeks each, after feature lags remove early weeks)
- **Date range:** May 2021 to October 2025
- **5 counties:** Kiambu, Kirinyaga, Mombasa, Nairobi, Uasin-Gishu

---

## 2. Model Training Pipeline (`src/models/train.py`)

### What we predict: Δ-price (price change)

Instead of predicting the absolute price (e.g., "KES 45"), we predict **how much the price will change from last week** (e.g., "+KES 1.2").

```
Target = price_change = price_this_week - price_last_week
```

Why? Price changes are more predictable than absolute prices. The model doesn't need to learn the overall price level — just the direction and magnitude of movement.

### The model: XGBoost

XGBoost is a **gradient boosting** algorithm. Think of it as building hundreds of small decision trees, where each new tree tries to fix the mistakes of all previous trees combined.

```
Tree 1: predicts Δ-price → has errors
Tree 2: tries to predict Tree 1's errors → reduces errors
Tree 3: tries to predict remaining errors → further reduces
... (300 trees total)
Final prediction = sum of all tree predictions
```

### Pooled training (one model for all counties)

All 5 counties' data is combined into one training set. A "county dummy" column tells the model which county each row belongs to.

**Advantage:** Counties with less data (e.g., Kiambu) benefit from patterns learned from counties with more data (e.g., Nairobi). The county dummies let the model adjust its predictions for each county's unique price level.

### Expanding window cross-validation

Instead of random train/test split (which cheats by using future data to predict the past), we use **temporal cross-validation**:

```
Fold 1: Train on weeks 1–100  → Test on weeks 101–130
Fold 2: Train on weeks 1–130  → Test on weeks 131–160
Fold 3: Train on weeks 1–160  → Test on weeks 161–190
Fold 4: Train on weeks 1–190  → Test on weeks 191–220
Fold 5: Train on weeks 1–220  → Test on weeks 221–250
```

This simulates how the model would perform in the real world — trained on past data, predicting the future.

### Performance metrics

| Metric | Value | Meaning |
|--------|-------|---------|
| **MASE** | 0.322 | < 1.0 means better than naive forecast (predict "no change"). 0.322 is excellent |
| **Directional Accuracy** | 75.5% | The model correctly predicts whether prices will go up or down 3 out of 4 times |
| **MAE** | 2.07 KES | Typical prediction error is about KES 2 per kg |
| **sMAPE** | 4.8% | Average percentage error is under 5% |

### What gets saved
- **`models/pooled_xgboost.pkl`** — the trained XGBoost model (431 KB)
- **`models/model_config.json`** — list of feature column names so the dashboard knows what the model expects
- **`models/model_evaluation.csv`** — per-county and overall performance numbers

---

## 3. Forecast Generation (how the dashboard predicts the future)

### The challenge of multi-step forecasting

The dashboard needs to predict 24+ weeks ahead, but the model only predicts **one week ahead**. To predict week 24, we must:

1. Predict week 1 → use that prediction to compute features for week 2
2. Predict week 2 → use that prediction to compute features for week 3
3. ... repeat 24 times

This is called **auto-regressive forecasting**. The problem: errors compound. A slightly-too-high prediction in week 1 causes week 2's features to also be too high, causing week 2's prediction to be even higher, and so on.

### How the dashboard solves this

The dashboard applies three fixes:

**A. Freeze trend features:** Instead of feeding predicted prices back into the model's lag features, we keep the lag features frozen at their last known actual values. This prevents the upward/downward spiral.

**B. Detrend:** The model was trained on 2021–2025 data which had an overall upward trend (inflation). The dashboard computes the recent average weekly price change and subtracts it from predictions, so only the "unexpected" part of the forecast matters.

**C. Dampening:** Longer-term forecasts are gradually pulled toward the current price. The farther out the prediction, the more conservative it becomes.

```
Forecast week 1:  100% of model signal
Forecast week 12:  70% of model signal
Forecast week 24:  40% of model signal
```

### Confidence intervals

The dashboard shows a **possible range** (80% confidence band) around each forecast:

```
Lower bound = forecast - 0.8 × 1.28 × √(week_number)
Upper bound = forecast + 0.8 × 1.28 × √(week_number)
```

The range widens for farther-out predictions — reflecting increasing uncertainty.

---

## 4. Dashboard (`src/dashboard/app.py`)

A 3-tab Streamlit web app with farmer-friendly language.

### Tab 1: 📈 Price Forecast
- Select your county and forecast horizon (8–30 weeks)
- **Signal banner:** Shows "Rising 🚀", "Falling 🔻", or "Stable ➡️" with plain-language advice
- **Chart:** Past prices (blue line) + Forecast (red dashed line) + Possible range (shaded band)
- **Table:** Week-by-week predicted prices

### Tab 2: 🏪 Compare Markets
- **Best market to SELL** (highest current price, highlighted green)
- **Best market to BUY** (lowest current price, highlighted blue)
- **Chart:** Forecast lines for all 5 counties overlaid for comparison
- **Table:** Ranked by forecasted price

### Tab 3: 🗓 Best Time & Tips
- **Best month to sell** (historical peak price month)
- **Best month to buy** (historical trough price month)
- **Monthly price bar chart** (green = below average, red = above average)
- **Tips cards:** Farmer advice vs Buyer advice based on current trend
- **Simple explanations** of what drives maize prices

### Sidebar KPIs
- Current price with weekly change arrow
- 4-week trend (up/down)
- All-time price range (min–max)

---

## 5. Deployment

- **Hosting:** Streamlit Cloud (free tier)
- **Code:** GitHub repository (`github.com/Timinah-rt/Maize_project`)
- **Auto-deploy:** Every push to `main` branch triggers a rebuild
- **URL:** `https://maizepriceguide.streamlit.app` (or similar *.streamlit.app URL)

---

## 6. File Structure

```
maize-forecasting/
├── streamlit_app.py          # Entry point for Streamlit Cloud
├── requirements.txt          # Dependencies
├── data/
│   └── features/
│       └── panel_features.csv  # Ready-to-use dataset (709 rows × 29 cols)
├── models/
│   ├── pooled_xgboost.pkl      # Trained XGBoost model
│   ├── model_config.json       # Feature column names
│   └── model_evaluation.csv    # Performance metrics
├── src/
│   ├── dashboard/
│   │   └── app.py              # Streamlit dashboard (3 tabs)
│   ├── data/
│   │   ├── clean.py            # Data cleaning script
│   │   └── features.py         # Feature engineering script
│   └── models/
│       └── train.py            # Model training pipeline
└── docs/
    ├── HOW_IT_WORKS.md         # This document
    ├── PROJECT_DOCUMENTATION.md # Full academic documentation
    └── Maize_Price_Forecasting_Presentation.pptx # PowerPoint slides
```

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run src/dashboard/app.py

# Re-train the model (if needed)
python src/models/train.py

# Re-generate features (if raw data changes)
python src/data/features.py
```
