# Weather Prediction App for Makueni County

This application predicts weather for Makueni County using historical weather data. It uses a Long Short-Term Memory (LSTM) neural network model to forecast temperature based on the past 30 days of weather data. The app is built with Flask to provide a web interface for users to enter a date and get temperature predictions.

## Files

- `data_collection.py`: Script to collect historical weather data from the OpenWeatherMap API and save it to `historical_weather_data.csv`.
- `data_processing.py`: Script to process the collected data and save it to `processed_weather_data.csv`.
- `prepare_data.py`: Script to prepare the data for the LSTM model and save the numpy arrays `X_train.npy`, `X_test.npy`, `y_train.npy`, `y_test.npy`.
- `train_model.py`: Script to build and train the LSTM model, and save the trained model to `lstm_weather_prediction_model.h5`.
- `app.py`: Flask application script to provide a web interface for weather prediction.
- `templates/index.html`: HTML template for the home page of the web application.
- `templates/result.html`: HTML template to display the prediction result.

## CSV Files

- `historical_weather_data.csv`: Contains raw historical weather data with columns for date, temperature, humidity, precipitation, and wind speed.
- `processed_weather_data.csv`: Processed weather data with missing values handled and necessary columns included.

## NPY Files

- `X_train.npy`: Training features for the LSTM model.
- `X_test.npy`: Testing features for the LSTM model.
- `y_train.npy`: Training labels for the LSTM model.
- `y_test.npy`: Testing labels for the LSTM model.

## How to Run

1. Collect historical weather data:
   ```bash
   python data_collection.py
   
2. Process the collected data:
   ```bash
   python data_processing.py

3. Prepare the data for model training:
   ```bash
   python prepare_data.py

4. Train the LSTM model:
   ```bash
   python train_model.py

5. Run the Flask application:
   ```bash
   python app.py

6. Install the required packages using:
   ```bash
   pip install Flask pandas numpy scikit-learn tensorflow requests
