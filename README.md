# Rainfall-prediction
The code generates a scatter plot of rainfall data for 10 years from 2010 to 2019 and uses linear regression to predict rainfall for the year 2020.

First, it imports necessary modules such as pandas, numpy, sklearn.linear_model, and matplotlib.pyplot. Then, an empty list called year_labels is created to store year labels, and a for loop is used to generate year labels from 2010 to 2019.

Next, a random rainfall data is generated using the NumPy's random.uniform() function with a low value of 50.0 and a high value of 200.0. The scatter plot is generated using the plt.scatter() function with the years on the x-axis and rainfall on the y-axis.

The X and y arrays are then created by reshaping the years and rainfall arrays into a 2D array to fit into a linear regression model using the LinearRegression() function from the scikit-learn library. The model is fitted to the data using the fit() method.

Finally, the predicted rainfall for the year 2020 is computed using the predict() method of the LinearRegression object, and the result is printed on the console.

Overall, the code demonstrates how to use linear regression to predict future values based on historical data.
