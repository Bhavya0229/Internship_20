import pandas as pd
data = pd.read_csv('cricket_salary_data.csv')
# regressor.score(features_train,features_label)
# regressor.score(features_test,labels_test)

data.isnull().any(axis = 0)
features = data.iloc[:,0:3].values
labels = data.iloc[:,3].values

from sklearn.impute import SimpleImputer
from numpy import nan

imputer = SimpleImputer(missing_values = nan, strategy = 'mean')

features[:,1:2] = imputer.fit_transform(features[:,1:2])






