# Female stats
import pandas as pd
female_df = pd.read_csv('Female_Stats.csv')
female_df.columns.tolist()
female_df.isnull().any(axis = 0)

features = female_df.iloc[:,1:3].values
labels = female_df.iloc[:,0].values

# task01:Build A Predictive Model And Conclude If Both Predictors 
#(Independent Variables) Are Significant For A Students’ Height Or Not?
#(Use pvalue concepts).

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
pred = regressor.predict(features_test)
pd.DataFrame(zip(pred, labels_test))

import statsmodels.api as sm
import numpy as np

features_sm = sm.add_constant(features)
regressor_ols = sm.OLS(labels, features_sm).fit()
regressor_ols.summary()

"""
as both columns ( mom and dad are having p values less than 5%, both 
                 heights are significant for student's height)
"""
"""
task02:
When Father’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Mother’s Height.
"""
print(regressor_ols.params[1])

"""
When Mother’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Father’s Height.
"""
print(regressor_ols.params[2])
