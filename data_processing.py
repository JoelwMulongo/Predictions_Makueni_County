import pandas as pd
from datetime import datetime

def process_weather_data():
    raw_data = pd.read_csv('historical_weather_data.csv')
    
    processed_data = []

    for day_data in raw_data['data']:
        for hourly_data in day_data['hourly']:
            date_time = datetime.fromtimestamp(hourly_data['dt'])
            temp = hourly_data['temp']
            humidity = hourly_data['humidity']
            weather = hourly_data['weather'][0]['description']
            processed_data.append([date_time, temp, humidity, weather])

    df = pd.DataFrame(processed_data, columns=['Date', 'Temperature', 'Humidity', 'Weather'])
    return df

weather_df = process_weather_data()
weather_df.to_csv('processed_weather_data.csv', index=False)
