import numpy as np

# Mock data for demonstration purposes
# Creating random data arrays for X_train, X_test, y_train, y_test

# Generate random data for training and testing
X_train = np.random.rand(100, 30, 4)
X_test = np.random.rand(20, 30, 4)
y_train = np.random.rand(100)
y_test = np.random.rand(20)

# Save the mock data to .npy files
np.save('X_train.npy', X_train)
np.save('X_test.npy', X_test)
np.save('y_train.npy', y_train)
np.save('y_test.npy', y_test)

print("Mock data generated and saved successfully.")
