import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the processed data
weather_df = pd.read_csv('processed_weather_data.csv')

# Scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(weather_df[['Temperature', 'Humidity']])

# Create sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length, 0])
    return np.array(X), np.array(y)

SEQ_LENGTH = 30  # Using past 30 days to predict the next day
X, y = create_sequences(scaled_data, SEQ_LENGTH)

# Split the data into training and testing sets
TRAIN_SIZE = int(len(X) * 0.8)
X_train, X_test = X[:TRAIN_SIZE], X[TRAIN_SIZE:]
y_train, y_test = y[:TRAIN_SIZE], y[TRAIN_SIZE:]

np.save('X_train.npy', X_train)
np.save('X_test.npy', X_test)
np.save('y_train.npy', y_train)
np.save('y_test.npy', y_test)
