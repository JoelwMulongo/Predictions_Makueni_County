from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os

app = Flask(__name__)
model = load_model('lstm_weather_prediction_model.h5')

# Load and preprocess the data
weather_df = pd.read_csv('processed_weather_data.csv', index_col='date', parse_dates=True)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(weather_df[['temperature', 'humidity', 'precipitation', 'wind_speed']])

def prepare_input(date, past_days=30):
    end_date = pd.to_datetime(date)
    start_date = end_date - pd.Timedelta(days=past_days)
    data = weather_df.loc[start_date:end_date].copy()
    if len(data) < past_days + 1:
        return None
    scaled_data = scaler.transform(data[['temperature', 'humidity', 'precipitation', 'wind_speed']])
    return np.array([scaled_data[:-1]])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    date = request.form['date']
    try:
        input_data = prepare_input(date)
        if input_data is None:
            return render_template('index.html', error='Not enough historical data to make a prediction.')
        prediction = model.predict(input_data)
        predicted_temperature = scaler.inverse_transform([np.concatenate((prediction[0], [0, 0, 0]))])[0][0]
        return render_template('result.html', date=date, temperature=predicted_temperature)
    except Exception as e:
        return render_template('index.html', error=f'An error occurred: {str(e)}')

if __name__ == '__main__':
    if not os.path.exists('static/temperature_plot.png'):
        import data_visualization
    app.run(debug=True)
