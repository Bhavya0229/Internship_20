#feature selection
import pandas as pd
dataset = pd.read_csv('Salary_Classification.csv')

dataset.columns.tolist()

dataset.dtypes
# to see any null value
dataset.isnull().any(axis=0)

# features and labels
features = dataset.iloc[:,0:4].values
labels = dataset.iloc[:,-1].values

#department columns
#we need to convert categorical data to numeric representation
#encode our categorical data in numeric
#onehotencoding

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )
import numpy as np
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

#backward elimination
import statsmodels.api as sm
import numpy as np
features = sm.add_constant(features)

"""
features_optimal = features[:,[0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_ols.summary()
regressor_ols.pvalues

features_optimal = features[:,[0,1,3,4,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_ols.summary()

features_optimal = features[:,[0,1,3,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_ols.summary()

features_optimal = features[:,[0,3,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_ols.summary()

features_optimal = features[:,[0,5]]
regressor_ols = sm.OLS(endog = labels, exog = features_optimal).fit()
regressor_ols.summary()
"""

features_optimal = features[:, [0,1,2,3,4,5]]

while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_optimal = np.delete(features_optimal, p_values.argmax(),1)
    else:
        break

    
print (features_optimal.shape)

