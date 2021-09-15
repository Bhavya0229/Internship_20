# classification model
"""
Perform Classification on the given dataset to predict if the mushroom is 
edible or poisonous w.r.t. it’s different attributes.

(you can perform on habitat, population and odor as the predictors)

Check accuracy of the model.
"""
# importing the dataset using pandas
import pandas as pd
mushroom_df = pd.read_csv('mushrooms.csv')

mushroom_df.columns.tolist()

# separating out features and labels

features = mushroom_df.iloc[:,[5,-2,-1]].values
labels = mushroom_df.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

le = LabelEncoder()
labels = le.fit_transform(labels)

#all columns in features need to be one hot encoded
cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0,1,2])], remainder = 'passthrough')
features = cTransformer.fit_transform(features).toarray()

# train-test-split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

# classification model
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors= 5, p = 2)
classifier.fit(features_train, labels_train)
pred = classifier.predict(features_test)

# confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(labels_test, pred)

# accuracy score of the model
from sklearn.metrics import accuracy_score
accuracy_score(labels_test, pred)




