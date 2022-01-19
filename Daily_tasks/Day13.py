import pandas as pd

dataset = pd.read_csv('student_scores.csv')

dataset.columns.tolist()


features = dataset['Hours'].values
labels = dataset['Scores'].values

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

features_train = features_train.reshape(20,1)

regressor.fit(features_train, labels_train)

features_test = features_test.reshape(5,1)

pred = regressor.predict(features_test)



pd.DataFrame(zip(pred, labels_test))





