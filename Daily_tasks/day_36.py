# NLP part-1
import pandas as pd

dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter = '\t')

features = dataset.iloc[:,0]
labels = dataset.iloc[:,1]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
features = cv.fit_transform(features)

features = features.toarray()

# train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#knn based model
from sklearn.neighbors import KNeighborsClassifier

model_knn  = KNeighborsClassifier()

model_knn.fit(features_train, labels_train)

print (model_knn.score(features_test, labels_test))

#lr based model

from sklearn.linear_model import LogisticRegression

model_lr = LogisticRegression()
model_lr.fit(features_train, labels_train)

print (model_lr.score(features_test, labels_test))


from sklearn.naive_bayes import GaussianNB

model_nb = GaussianNB()

model_nb.fit(features_train, labels_train)

print (model_nb.score(features_test, labels_test))

#for a single review


reviewText = 'I love this restaurant'

reviewText = cv.transform([reviewText])

model_lr.predict(reviewText)