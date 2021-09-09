import pandas as pd

foodtruck_df = pd.read_csv('Foodtruck.csv')
foodtruck_df.columns.tolist()

features = foodtruck_df['Population'].values
labels = foodtruck_df['Profit'].values

import matplotlib.pyplot as plt
plt.scatter(features,labels)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
features = features.reshape(97,1)
regressor.fit(features,labels)

m = regressor.coef_
c = regressor.intercept_

x = 3.073
(m*x) + c

regressor.predict([[3.073]])
regressor.predict([[33.4]])
regressor.predict(features)
plt.scatter(features,labels)
plt.plot(features, regressor.predict(features))

#As profit is coming negative, so it would be a loss
#hence not recommended to open the outlet in Jaipur