import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Initialize an empty list to store the year labels
year_labels = []

# Use a for loop to generate the year labels from 2010 to 2020
for year in range(2010, 2019):
    year_labels.append(str(year))
rainfall = np.random.uniform(low=50.0, high=200.0, size=10)

plt.scatter(years, rainfall)
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.show()

# Reshape the data to create a 2D array for fitting the model
X = years.reshape(-1, 1)
y = rainfall.reshape(-1, 1)

# Create a linear regression object and fit the data
model = LinearRegression()
model.fit(X, y)

# Predict the rainfall for 2020
predicted_rainfall = model.predict([[2020]])

print(f"The predicted rainfall for 2020 is {predicted_rainfall[0][0]} mm")




