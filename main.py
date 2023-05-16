import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt


# Read the rainfall data from a CSV file
data = pd.read_csv('rainfall_data.csv')

# Preprocess the data
data['ds'] = pd.to_datetime(data['date'])
data['y'] = data['rainfall']

# Create and fit the Prophet model
model = Prophet()
model.fit(data)

# Create a future dataframe for prediction
future = model.make_future_dataframe(periods=365)  # Predict for the next 365 days

# Make predictions
forecast = model.predict(future)

# Plot the forecast
model.plot(forecast, xlabel='Date', ylabel='Rainfall')
model.plot_components(forecast)  # Plot the components (trend, weekly seasonality, yearly seasonality)

# Access individual components and predictions
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

# Access the forecasted values
predicted_rainfall = forecast[['ds', 'yhat']].tail(365)

# Save the forecast to a CSV file
predicted_rainfall.to_csv('predicted_rainfall.csv', index=False)

# Actual rainfall values
actual_rainfall = data['y'].values

# Predicted rainfall values
predicted_rainfall = forecast['yhat'].values[:-365]  # Exclude the forecasted values

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(actual_rainfall, predicted_rainfall))
print('Root Mean Squared Error (RMSE):', rmse)


# Scatter plot of trends
plt.scatter(data['ds'], data['y'], color='blue', label='Actual Rainfall')
plt.scatter(forecast['ds'][:-365], forecast['yhat'][:-365], color='red', label='Predicted Rainfall')
plt.xlabel('Date')
plt.ylabel('Rainfall')
plt.legend()
plt.title('Scatter Plot of Actual and Predicted Rainfall Trends')
plt.show()


