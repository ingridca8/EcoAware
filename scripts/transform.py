# scripts/transform.py
import pandas as pd

def transform_air_quality_data(df):
    # Keep relevant columns
    df = df[['city', 'parameter', 'value', 'unit', 'date.utc']]
    
    # Rename columns
    df.rename(columns={'date.utc': 'datetime'}, inplace=True)
    
    # Convert datetime
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    # Drop missing values
    df.dropna(inplace=True)
    
    # Calculate average value per city and parameter
    df_avg = df.groupby(['city', 'parameter']).agg({'value': 'mean'}).reset_index()
    
    return df_avg