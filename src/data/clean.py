import pandas as pd
import numpy as np
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent.parent / 'data' / 'raw'
PROCESSED_DIR = Path(__file__).parent.parent.parent / 'data' / 'processed'

def clean_kamis(df):
    df = df.copy()
    df = df[df['Commodity_Classification'].str.contains('White_Maize', na=False)].copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['county'] = df['county'].str.strip().str.title()
    df['county'] = df['county'].replace({
        'Uasin Gishu': 'Uasin-Gishu',
        'Uasingishu': 'Uasin-Gishu',
        'Nairobi City': 'Nairobi',
        'Kiambu County': 'Kiambu'
    })
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    df['wholesale'] = pd.to_numeric(df['wholesale'], errors='coerce')
    unrealistic = (df['wholesale'] < 10) | (df['wholesale'] > 500)
    df = df[~unrealistic]
    for col in ['wholesale', 'retail']:
        if col in df.columns:
            df[col] = df.groupby('county')[col].transform(lambda x: x.ffill().bfill())
            df[col] = df[col].fillna(df[col].median())
    if 'supplyvolume' in df.columns:
        df['supplyvolume'] = df.groupby('county')['supplyvolume'].transform(lambda x: x.ffill().fillna(x.median()))
        df['supplyvolume'] = df['supplyvolume'].fillna(df['supplyvolume'].median())
    if 'market' in df.columns:
        df['market'] = df['market'].str.strip().str.title()
    df = df.drop_duplicates(subset=['county', 'date', 'market'], keep='first')
    return df

def clean_agri(df):
    df = df.copy()
    df = df[df['Commodity_Classification'].str.contains('White_Maize', na=False)].copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['county'] = df['county'].str.strip().str.title()
    df['county'] = df['county'].replace({
        'Uasin Gishu': 'Uasin-Gishu',
        'Uasingishu': 'Uasin-Gishu',
        'Nairobi City': 'Nairobi'
    })
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    df['wholesale'] = pd.to_numeric(df['wholesale'], errors='coerce')
    unrealistic = (df['wholesale'] < 10) | (df['wholesale'] > 500)
    df = df[~unrealistic]
    df['wholesale'] = df.groupby('county')['wholesale'].transform(lambda x: x.ffill().bfill())
    df['wholesale'] = df['wholesale'].fillna(df['wholesale'].median())
    df = df.drop_duplicates(subset=['county', 'date'], keep='first')
    return df

def clean_weather(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['county'] = df['county'].str.strip().str.title()
    df['county'] = df['county'].replace({
        'Uasin Gishu': 'Uasin-Gishu',
        'Uasingishu': 'Uasin-Gishu',
        'Nairobi City': 'Nairobi',
        'Kiambu County': 'Kiambu'
    })
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    temp_cols = ['temp_max_c', 'temp_min_c', 'temp_avg_c']
    for col in temp_cols:
        if col in df.columns:
            df[col] = df.groupby('county')[col].transform(lambda x: x.interpolate(method='linear', limit_direction='both'))
            df[col] = df[col].fillna(df[col].mean())
    rain_cols = ['precipitation_mm', 'rain_mm', 'precipitation_hours']
    for col in rain_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)
            df[col] = df.groupby('county')[col].transform(lambda x: x.ffill().fillna(0))
    wind_cols = ['wind_speed_max_kmh', 'wind_gusts_max_kmh']
    for col in wind_cols:
        if col in df.columns:
            df[col] = df.groupby('county')[col].transform(lambda x: x.ffill().fillna(x.median()))
            df[col] = df[col].fillna(df[col].median())
    if 'temp_max_c' in df.columns:
        df['temp_max_c'] = df['temp_max_c'].clip(lower=10, upper=40)
    if 'temp_min_c' in df.columns:
        df['temp_min_c'] = df['temp_min_c'].clip(lower=5, upper=30)
    if 'temp_avg_c' in df.columns:
        df['temp_avg_c'] = df['temp_avg_c'].clip(lower=8, upper=35)
    if 'rain_mm' in df.columns:
        df['rain_mm'] = df['rain_mm'].clip(upper=200)
    if 'wind_speed_max_kmh' in df.columns:
        df['wind_speed_max_kmh'] = df['wind_speed_max_kmh'].clip(upper=150)
    df = df.drop_duplicates(subset=['county', 'date'], keep='first')
    return df

def main():
    kamis_df = pd.read_csv(RAW_DIR / 'kamis_maize_prices.csv')
    agri_df = pd.read_csv(RAW_DIR / 'agriBORA_maize_prices.csv')
    weather_df = pd.read_csv(RAW_DIR / 'weather_kenya_all_counties_2021_2025 (2).csv')
    kamis_clean = clean_kamis(kamis_df)
    agri_clean = clean_agri(agri_df)
    weather_clean = clean_weather(weather_df)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    kamis_clean.to_csv(PROCESSED_DIR / 'kamis_clean.csv', index=False)
    agri_clean.to_csv(PROCESSED_DIR / 'agri_clean.csv', index=False)
    weather_clean.to_csv(PROCESSED_DIR / 'weather_clean.csv', index=False)
    print(f'KAMIS cleaned: {kamis_clean.shape}')
    print(f'AgriBORA cleaned: {agri_clean.shape}')
    print(f'Weather cleaned: {weather_clean.shape}')
    print(f'Processed data saved to {PROCESSED_DIR}')

if __name__ == '__main__':
    main()
