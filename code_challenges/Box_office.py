import pandas as pd

movies_df = pd.read_csv('Box_Office.csv')
movies_df.columns.tolist()

features = movies_df.iloc[:,0:1].values
labels_1 = movies_df.iloc[:,1:2].values
labels_2 = movies_df.iloc[:,2:3].values

import matplotlib.pyplot as plt
plt.scatter(features,labels_1,labels_2)

from sklearn.linear_model import LinearRegression

regressor_1 = LinearRegression()
regressor_2 = LinearRegression()

features = features.reshape(9,1)
regressor_1.fit(features,labels_1)
regressor_2.fit(features,labels_2)

regressor_1.predict([[10]])
regressor_2.predict([[10]])

plt.scatter(features,labels_1,labels_2)
plt.plot(features,regressor_1.predict(features),regressor_2.predict(features))




