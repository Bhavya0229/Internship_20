# IQ SIZE PREDICTION

import pandas as pd
IQ_df = pd.read_csv('IQ_Size.csv')
IQ_df.columns.tolist()
IQ_df.isnull().any(axis = 0)

"""
Task01:
What is the IQ of an individual with a given 
brain size of 90, height of 70 inches, and weight 150 pounds ?
"""

features = IQ_df.iloc[:,1:].values
labels = IQ_df.iloc[:,0].values

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state= 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
pred = regressor.predict(features_test)
pd.DataFrame(zip(pred, labels_test))

regressor.predict([[90,70,150]])
# array([105.76890364])
"""
Task02:
Are a person's brain size and body size (Height and weight) predictive 
of his or her intelligence?
"""
import statsmodels.api as sm
import numpy as np
features = sm.add_constant(features)
features_optimal = features[:,[0,1,2,3]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()

# drop weight
features_optimal = features[:,[0,1,2]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()

# drop constant
features_optimal = features[:,[1,2]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()

# drop height
features_optimal = features[:,[1]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()

print ("Brain Size is the only factor which is more useful in predicting intelligence.")

