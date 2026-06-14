import pandas as pd
import numpy as np
from pathlib import Path

PROCESSED_DIR = Path(__file__).parent.parent.parent / "data" / "processed"
FEATURES_DIR = Path(__file__).parent.parent.parent / "data" / "features"

# Kenya maize seasons
# Long rains: Planting Mar-Apr, Harvest Aug-Sep
# Short rains: Planting Oct-Nov, Harvest Feb-Mar
def get_season(date):
    month = date.month
    if month in [3, 4, 8, 9]:
        return 'long_rains'
    elif month in [10, 11, 2, 3]:
        return 'short_rains'
    else:
        return 'off_season'

# Producer vs Consumer counties
PRODUCER_COUNTIES = [
    'Uasin-Gishu', 'Trans-Nzoia', 'Nakuru', 'Baringo', 'Laikipia',
    'Narok', 'Kericho', 'Bungoma', 'Kakamega', 'Nandi'
]

def create_features():
    """Create feature-rich panel dataset"""
    # Load processed data
    kamis = pd.read_csv(PROCESSED_DIR / "kamis_clean.csv", parse_dates=['date'])
    agri = pd.read_csv(PROCESSED_DIR / "agri_clean.csv", parse_dates=['date'])
    weather = pd.read_csv(PROCESSED_DIR / "weather_clean.csv", parse_dates=['date'])

    # Load economic data
    usd_kes = pd.read_csv(PROCESSED_DIR.parent / "raw" / "usd_kes_rates.csv", parse_dates=['date'])
    cpi = pd.read_csv(PROCESSED_DIR.parent / "raw" / "kenya_cpi.csv", parse_dates=['date'])
    
    
    # Create week_start for aggregation
    for df in [kamis, agri, weather]:
        df['week_start'] = df['date'].dt.to_period('W').apply(lambda p: p.start_time)
    
    # Aggregate weekly
    kamis_weekly = kamis.groupby(['county', 'week_start'])['wholesale'].agg(['mean', 'std']).reset_index()
    kamis_weekly.columns = ['county', 'week_start', 'kamis_price', 'kamis_std']
    
    agri_weekly = agri.groupby(['county', 'week_start'])['wholesale'].agg(['mean', 'std']).reset_index()
    agri_weekly.columns = ['county', 'week_start', 'agri_price', 'agri_std']
    
    weather_weekly = weather.groupby(['county', 'week_start']).agg({
        'temp_avg_c': 'mean',
        'temp_max_c': 'max',
        'temp_min_c': 'min',
        'rain_mm': 'sum',
        'wind_speed_max_kmh': 'max'
    }).reset_index()
    
    # Merge datasets
    panel = kamis_weekly.copy()
    panel = pd.merge(panel, agri_weekly, on=['county', 'week_start'], how='outer')
    panel = pd.merge(panel, weather_weekly, on=['county', 'week_start'], how='left')

    # Merge economic data (weekly aggregation)
    usd_kes['week_start'] = usd_kes['date'].dt.to_period('W').apply(lambda p: p.start_time)
    usd_kes_weekly = usd_kes.groupby('week_start')['usd_kes'].mean().reset_index()

    cpi['week_start'] = cpi['date'].dt.to_period('W').apply(lambda p: p.start_time)
    cpi_weekly = cpi.groupby('week_start').agg({'cpi': 'mean', 'inflation_rate': 'mean'}).reset_index()

    panel = pd.merge(panel, usd_kes_weekly, on='week_start', how='left')
    panel = pd.merge(panel, cpi_weekly, on='week_start', how='left')
    panel = panel.sort_values(['county', 'week_start']).reset_index(drop=True)

    # Forward fill economic data (same for all counties)
    panel['usd_kes'] = panel['usd_kes'].ffill().bfill()
    panel['cpi'] = panel['cpi'].ffill().bfill()
    panel['inflation_rate'] = panel['inflation_rate'].ffill().bfill()
    
    # Fill missing values by county
    for county in panel['county'].unique():
        mask = panel['county'] == county
        for col in ['kamis_price', 'agri_price', 'temp_avg_c', 'rain_mm']:
            if col in panel.columns:
                panel.loc[mask, col] = panel.loc[mask, col].ffill().bfill()
    
    # Create price source (AgriBORA primary, KAMIS fallback)
    panel['price'] = panel['agri_price'].fillna(panel['kamis_price'])
    
    # === FEATURE ENGINEERING ===
    
    # 1. Lag features (7, 14, 30 days worth of weeks ~ 1, 2, 4 weeks)
    for lag in [1, 2, 4, 8, 12]:
        panel[f'price_lag_{lag}w'] = panel.groupby('county')['price'].shift(lag)
    
    # 2. Rolling features
    for window in [4, 8, 12]:
        panel[f'price_ma_{window}w'] = panel.groupby('county')['price'].transform(
            lambda x: x.shift(1).rolling(window).mean()
        )
        panel[f'price_std_{window}w'] = panel.groupby('county')['price'].transform(
            lambda x: x.shift(1).rolling(window).std()
        )
    
    # 3. Seasonal features
    panel['month'] = panel['week_start'].dt.month
    panel['season'] = panel['week_start'].apply(get_season)
    panel['is_long_rains'] = (panel['season'] == 'long_rains').astype(int)
    panel['is_short_rains'] = (panel['season'] == 'short_rains').astype(int)
    panel['is_harvest'] = panel['month'].isin([8, 9, 2, 3]).astype(int)
    
    # 4. County type features
    panel['is_producer'] = panel['county'].isin(PRODUCER_COUNTIES).astype(int)
    panel['is_consumer'] = (~panel['county'].isin(PRODUCER_COUNTIES)).astype(int)
    
    # 5. Weather rolling features
    for window in [4, 8]:
        panel[f'rain_sum_{window}w'] = panel.groupby('county')['rain_mm'].transform(
            lambda x: x.shift(1).rolling(window).sum()
        )
        panel[f'temp_avg_{window}w'] = panel.groupby('county')['temp_avg_c'].transform(
            lambda x: x.shift(1).rolling(window).mean()
        )
    
    # 6. Time features
    panel['week_of_year'] = panel['week_start'].dt.isocalendar().week
    panel['year'] = panel['week_start'].dt.year
    panel['days_from_start'] = (panel['week_start'] - panel['week_start'].min()).dt.days
    
    # Drop rows with NaN in key features (from lags)
    panel = panel.dropna(subset=['price']).reset_index(drop=True)
    
    # Save features
    FEATURES_DIR.mkdir(parents=True, exist_ok=True)
    panel.to_csv(FEATURES_DIR / "panel_features.csv", index=False)
    
    print(f"Features created: {panel.shape}")
    print(f"Columns: {list(panel.columns)}")
    return panel

if __name__ == "__main__":
    create_features()
