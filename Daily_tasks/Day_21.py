# classification using KNN algorithm

import pandas as pd

dataset = pd.read_csv('caesarian.csv')
dataset.shape
dataset.columns.tolist()
dataset.isnull().any(axis = 0)
dataset.dtypes

# features and labels
features = dataset.iloc[:,0:5]
labels = dataset.iloc[:,5]

# train test split
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state= 0)

# build the model
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5, p = 1)
#p = 1, manhanttan
#p = 2, euclidian
classifier.fit(features_train, labels_train)

pred = classifier.predict(features_test)

# confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(labels_test, pred)
x = [22, 1, 0, 1, 0]

import numpy as np

x = np.array(x)

x =  x.reshape(1,5)

classifier.predict(x)
