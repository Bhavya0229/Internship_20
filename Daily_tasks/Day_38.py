# NLP part-3
import pandas as pd

dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter = '\t')

features = dataset.iloc[:,0]
labels = dataset.iloc[:,1]

# data cleaning activity
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#lets take the first review for cleanup
print(features[2])
dataset['Review'][2]

# search for special character set, using re module
# not belonging to a - z or A - Z

import re
review = re.sub('[^a-zA-z]',' ',dataset['Review'][2])
review = review.lower()
review = review.split()

#remove the stopwords
review = [word for word in review if not word in stopwords.words('english')]

#stemming
ps = PorterStemmer()
review = [ps.stem(word) for word in review]
review = " ".join(review)

corpus = []

for i in range(0, 1000):

    review = re.sub('[^a-zA-Z]', ' ',  dataset['Review'][i])

    review = review.lower()
    
    review = review.split()
    
    #remove the stopwords
    review = [word for word in review if not word in stopwords.words('english')]
    
    #stemming
    ps  = PorterStemmer()
    
    review = [ps.stem(word) for word in review]
    
    review = " ".join(review)
    
    corpus.append(review)

# Tfidf vectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfv = TfidfVectorizer(min_df=5)
features = tfidfv.fit_transform(corpus).toarray()


# train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

#lr based model

from sklearn.linear_model import LogisticRegression

model_lr = LogisticRegression()
model_lr.fit(features_train, labels_train)

print (model_lr.score(features_test, labels_test))


#for a single review


reviewText = 'bad service'

reviewText = tfidfv.transform([reviewText])

model_lr.predict(reviewText)



