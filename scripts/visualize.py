# scripts/visualize.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

def visualize_air_quality_data(db_path="data/air_quality_data.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM air_quality", conn)
    conn.close()
    
    # Pivot data for plotting
    pivot_df = df.pivot(index='parameter', columns='city', values='value')
    
    # Plotting
    pivot_df.plot(kind='bar', figsize=(12, 6))
    plt.title("Average Pollutant Levels by City")
    plt.xlabel("Pollutant Parameter")
    plt.ylabel("Average Value")
    plt.legend(title="City")
    plt.tight_layout()
    plt.show()