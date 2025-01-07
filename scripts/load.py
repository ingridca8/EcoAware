# scripts/load.py
import sqlite3

def load_data_to_db(df, db_path="data/air_quality_data.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("air_quality", conn, if_exists="replace", index=False)
    conn.close()
    print("Data loaded into database.")