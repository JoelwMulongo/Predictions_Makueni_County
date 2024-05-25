from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = load_model('lstm_weather_prediction_model.h5')

# Load and preprocess the data
weather_df = pd.read_csv('processed_weather_data.csv', index_col='Date', parse_dates=True)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(weather_df[['Temperature', 'Humidity']])

def prepare_input(date, past_days=30):
    end_date = pd.to_datetime(date)
    start_date = end_date - pd.Timedelta(days=past_days)
    past_data = weather_df.loc[start_date:end_date].values
    if len(past_data) < past_days:
        raise ValueError("Not enough data available")
    past_data_scaled = scaler.transform(past_data)
    return np.array([past_data_scaled])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    date = request.form['date']
    try:
        input_data = prepare_input(date)
        prediction_scaled = model.predict(input_data)
        prediction = scaler.inverse_transform(np.concatenate([prediction_scaled, np.zeros((1, 1))], axis=1))[0, 0]
        return render_template('result.html', prediction=prediction, date=date)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
