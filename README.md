# 🌽 Maize Price Forecasting Project

A machine learning pipeline for forecasting maize prices in Kenya using historical price data and weather features.

## Project Structure

```
maize-forecasting/
├── data/
│   ├── raw/              # Original datasets
│   ├── processed/        # Cleaned datasets
│   └── features/         # Feature-engineered data
├── src/
│   ├── data/            # Data cleaning and feature modules
│   │   ├── clean.py     # Data cleaning functions
│   │   └── features.py  # Feature engineering
│   ├── models/          # Model training and evaluation
│   │   └── train.py     # Training pipeline
│   └── dashboard/       # Streamlit dashboard
│       └── app.py       # Visualization dashboard
├── models/              # Trained model artifacts
├── notebooks/           # Jupyter notebooks for exploration
├── run.py              # Main pipeline runner
└── requirements.txt    # Python dependencies
```

## Datasets

- **KAMIS**: Kenya Agricultural Market Information System prices (retail/wholesale)
- **AgriBORA**: Transaction-based wholesale maize prices
- **Weather**: Daily weather data for all Kenyan counties (2021-2025)

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the full pipeline:**
   ```bash
   python run.py
   ```

3. **Launch the dashboard:**
   ```bash
   streamlit run src/dashboard/app.py
   ```

## Features

- **Data Cleaning**: Automated cleaning with outlier detection and missing value handling
- **Feature Engineering**: Lag features, rolling statistics, seasonal flags, producer/consumer county classification
- **Models**: Ridge, Random Forest, Gradient Boosting, XGBoost, SARIMA, LSTM
- **Evaluation**: TimeSeriesSplit validation, MAE/RMSE/MAPE/R2 metrics
- **Dashboard**: Interactive visualization of historical prices and forecasts

## Target Counties

- Kiambu
- Kirinyaga
- Mombasa
- Nairobi
- Uasin-Gishu

## Improvements Made

✅ Fixed `kais_clean` typo in original notebook  
✅ Removed redundant weather cleaning code  
✅ Added lag/rolling features (1, 2, 4, 8, 12 weeks)  
✅ Added maize season flags (long rains, short rains, harvest)  
✅ Added producer/consumer county classification  
✅ Modularized code into reusable scripts  
✅ Implemented multiple model types with hyperparameter tuning  
✅ Added TimeSeriesSplit for proper validation  
✅ Built Streamlit dashboard for visualization  
✅ Added model evaluation with metrics comparison  

## Next Steps

- Add SHAP interpretability analysis
- Add 95% prediction intervals
- Source Kenya CPI and USD-KES exchange rate data
- Ensemble top-performing models
- Add naive baselines (persistence, seasonal naive) for benchmark
