# DBSCAN 

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]

features, labels = make_blobs(n_samples = 750, centers= centers,cluster_std=0.4,
                              random_state=0)
print(features)
print(labels)

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

features = StandardScaler().fit_transform(features)
#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(features)
labels_pred = db.labels_ # belongs to which cluster id
print(labels_pred)

# Plot result
import matplotlib.pyplot as plt


plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+' )
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o' )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s' )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*' )
