# scripts/extract.py
import requests
import pandas as pd

'''def extract_air_quality_data(cities):
    base_url = "https://api.openaq.org/v2/measurements"
    all_data = []

    for city in cities:
        params = {
            "city": city,
            "limit": 1000,
            "sort": "desc",
            "order_by": "datetime"
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            all_data.extend(results)
            print(f"Data fetched for {city}")
        else:
            print(f"Failed to fetch data for {city}")

    # Convert to DataFrame
    df = pd.json_normalize(all_data)
    return df
'''
def fetch_weather_data(city):
    base_url = "https://api.openaq.org/v2/measurements"
    params = {
        "city": city,
        "limit": 1000,
        "sort": "desc",
        "order_by": "datetime"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()  # Return JSON data
    else:
        print(f"Failed to fetch data for {city}: {response.status_code}, {response.text}")
        return None  # Return None if the request failed

def extract_air_quality_data(cities):
    all_data = []

    for city in cities:
        data = fetch_weather_data(city)
        if data and "results" in data:
            all_data.extend(data["results"])
        else:
            print(f"No results found for {city} or invalid response.")
    
    if not all_data:
        print("No data extracted. Check API responses or city names.")
    
    # Convert to DataFrame
    df = pd.json_normalize(all_data) if all_data else pd.DataFrame()  # Return empty DataFrame if no data
    return df