"""
In 1981, 78 bluegills were randomly sampled from Lake Mary in Minnesota. 
The researchers (Cook and Weisberg, 1999) measured and recorded the 
following data:
(Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish.


How is the length of a bluegill fish best related to its age? 
(Linear/Quadratic nature?)

What is the length of a randomly selected five-year-old bluegill fish? 
Perform polynomial regression on the dataset.
"""
# importing the pandas and reading the csv file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
blue_df = pd.read_csv('bluegills.csv')

blue_df.shape
# checking for any null value
blue_df.isnull().any(axis = 0)

# separating out features and labels
features = blue_df.iloc[:,0:1].values
labels = blue_df.iloc[:,1:2].values
plt.scatter(features, labels)

# simple linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)
regressor.predict([[5]])
# array([[174.21045499]])
plt.scatter(features, labels)
plt.plot(features, regressor.predict(features), color = 'red')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

# polynomial regression model
from sklearn.preprocessing import PolynomialFeatures

"""
features_higher_degree = PolynomialFeatures(degree = 2)
features_ndata = features_higher_degree.fit_transform(features)
regressor_ndata = LinearRegression()

regressor_ndata.fit(features_ndata, labels)

plt.scatter(features, labels)
plt.plot(features, regressor_ndata.predict(features_higher_degree.transform(features)), color = 'red')
"""
higher_degree_gen = PolynomialFeatures(degree = 2)
features_poly = higher_degree_gen.fit_transform(features)
regressor_poly = LinearRegression()
regressor_poly.fit(features_poly, labels)

features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(len(features_grid), 1)
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, regressor_poly.predict(higher_degree_gen.fit_transform(features_grid)), color = 'blue')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

regressor_poly.predict(higher_degree_gen.fit_transform([[5]]))
# array([[165.90231606]])

