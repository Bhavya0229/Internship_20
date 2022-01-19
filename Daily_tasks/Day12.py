# Linear Regression

import pandas as pd

dataset = pd.read_csv('student_scores.csv')

dataset.columns.tolist()
dataset.isnull().any(axis = 0)

features = dataset['Hours'].values
labels = dataset['Scores'].values

import matplotlib.pyplot as plt
plt.scatter(features,labels)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

features = features.reshape(25,1)

regressor.fit(features,labels)

m = regressor.coef_
c = regressor.intercept_

x = 9
(m*x + c)

regressor.predict([[9]])
regressor.predict(features)
plt.scatter(features,labels)
plt.plot(features, regressor.predict(features))