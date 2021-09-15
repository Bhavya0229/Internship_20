"""
Code Task

The datasets consists of several medical predictor variables and one target variable, Outcome. 
Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

perform classification and build a machine learning model by performing standard scaling to accurately predict whether or not the patients in the 
dataset have diabetes or not?
"""
import pandas as pd
diabetes_df = pd.read_csv('diabetes.csv')

diabetes_df.columns.tolist()

diabetes_df.isnull().any(axis = 0)

# separating out features and labels
features = diabetes_df.iloc[:,0:8].values
labels = diabetes_df.iloc[:,8].values


# train test split
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2,random_state=42)

# feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# build the model
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, p = 2, metric='minkowski')

# fit into classification model
classifier.fit(features_train, labels_train)
pred = classifier.predict(features_test)

# import confusion matrix and check accuracy score

from sklearn.metrics import confusion_matrix, accuracy_score
confusion_matrix(labels_test, pred)
accuracy_score(labels_test, pred)

# feature selection
import statsmodels.api as sm
import numpy as np

"""
features = sm.add_constant(features)
features_optimal = features[:,[0,1,2,3,4,5,6,7,8]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()

# drop 4 column
features_optimal = features[:,[0,1,2,3,5,6,7,8]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()

# drop insulin column
features_optimal = features[:,[0,1,2,3,6,7,8]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()

# drop age column
features_optimal = features[:,[0,1,2,3,6,7]]
regressor_ols = sm.OLS(labels, features_optimal).fit()
regressor_ols.summary()


regressor_ols.pvalues
print (features_optimal.shape)
"""
features = sm.add_constant(features)
features_optimal = features[:,[0,1,2,3,4,5,6,7,8]]
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_optimal = np.delete(features_optimal, p_values.argmax(),1)
    else:
        break
