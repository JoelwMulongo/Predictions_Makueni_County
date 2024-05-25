import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = 'your_openweathermap_api_key'
LAT = -1.8034  # Latitude for Makueni County
LON = 37.6297  # Longitude for Makueni County
START_DATE = '2010-01-01'
END_DATE = '2023-12-31'

def get_weather_data(api_key, lat, lon, start_date, end_date):
    weather_data = []
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)

    while start <= end:
        timestamp = int(start.timestamp())
        url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        weather_data.append(data)
        start += delta

    return weather_data

weather_data = get_weather_data(API_KEY, LAT, LON, START_DATE, END_DATE)
pd.DataFrame(weather_data).to_csv('historical_weather_data.csv', index=False)
