"""
Suppose you are the manager of a bank and you have the problem of 
discriminating between genuine and counterfeit banknotes. You are measuring 
several distances on the banknote and the width and height of it.

Measuring these values of about 100 genuine and 100 counterfeit banknotes, 
Use the data set to set up a logical regression and is capable of 
discriminating between genuine and counterfeit money classification. 
(Import banknotes.csv)

(this data set contains data on Swiss francs currency; it has been obtained 
courtesy of H. Riedwyl )

Check the accuracy of your model using confusion matrix.

Then use k-fold cross validation to find actual mean accuracy of your model.

file_name - "banknotes.py"

"""

# importing the libraries
import pandas as pd

# importing the dataset
dataset = pd.read_csv('banknotes.csv')

dataset.columns.tolist()

# checking out missing values
dataset.isnull().any(axis = 0)

# separating out features and labels
features = dataset.iloc[:,1:-1].values
labels = dataset.iloc[:,-1].values

# splitting the dataset into training set and testing set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

# fitting logistic regression to the training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(features_train,labels_train)

# predicting the test results
labels_pred = classifier.predict(features_test)

# confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)

# accuracy score of the model
from sklearn.metrics import accuracy_score
accuracy_score(labels_test, labels_pred)

# applying k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier,X = features_train, y = labels_train, cv = 10)
print ("accuracies is ", accuracies)
print ("mean accuracy is",accuracies.mean())


