import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
weather_df = pd.read_csv('processed_weather_data.csv')

# Plot historical temperature data
plt.figure(figsize=(14, 7))
plt.plot(weather_df['date'], weather_df['temperature'], label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Historical Temperature Data for Makueni County')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image
plt.savefig('static/temperature_plot.png')
plt.show()
