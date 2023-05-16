# Rainfall-prediction
We have a CSV file named 'rainfall_data.csv' containing two columns: 'date' and 'rainfall'.

The code uses Prophet to fit the model to the data and make future predictions. We create a future dataframe using the make_future_dataframe function and specify the number of days to predict (365 days in this case). After making the predictions, the code plots the forecasted rainfall using model.plot. Additionally, you can access individual components and predictions using the forecast dataframe. Finally, the forecasted rainfall values are saved to a CSV file named 'predicted_rainfall.csv'.
