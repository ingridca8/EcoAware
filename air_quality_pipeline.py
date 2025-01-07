# air_quality_pipeline.py
from scripts.extract import extract_air_quality_data
from scripts.transform import transform_air_quality_data
from scripts.load import load_data_to_db
from scripts.visualize import visualize_air_quality_data

def main():
    cities = ["Delhi", "Los Angeles", "Beijing", "Paris", "Sydney"]
    print("Starting Air Quality ETL Pipeline...")
    
    # Extract
    print("Extracting data...")
    raw_data = extract_air_quality_data(cities)
    
    # Transform
    print("Transforming data...")
    processed_data = transform_air_quality_data(raw_data)
    
    # Load
    print("Loading data into database...")
    load_data_to_db(processed_data)
    
    # Visualize
    print("Creating visualizations...")
    visualize_air_quality_data()

if __name__ == "__main__":
    main()