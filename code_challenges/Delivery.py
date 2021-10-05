"""
Data Source File: deliveryfleet.csv

In this code challenge we need two driver features: 
mean distance driven per day (Distance_Feature) 
and 
the mean percentage of time a driver was > 5 mph over the 
speed limit (Speeding_Feature).

Perform K-means clustering to distinguish urban drivers 
and rural drivers. Label accordingly for the 2 groups.

Perform K-means clustering again to further distinguish 
speeding drivers from those who follow speed limits, 
in addition to the rural vs. urban division.
Label accordingly for the 4 groups.
"""

# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing the dataset
dataset = pd.read_csv('deliveryfleet.csv')
dataset.columns.tolist()
dataset.isnull().any(axis = 0)

# extracting the features
features = dataset.iloc[:,[1,2]].values

# visualizing the data
plt.scatter(features[:,0],features[:,1])
plt.show()

# elbow method 
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)  # we have not used the fit_predict
    wcss.append(kmeans.inertia_)
print(wcss)

# plotting wcss
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# fitting kmeans model
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'k-means++',random_state=0)
cluster_pred = kmeans.fit_predict(features)
print(cluster_pred)

# visualising the clusters
plt.scatter(features[cluster_pred == 0, 0], features[cluster_pred == 0, 1],s=100, c = 'blue', label = 'Cluster 1')
plt.scatter(features[cluster_pred == 1, 0], features[cluster_pred == 1, 1],s=100, c = 'red', label = 'Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],s=300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of Drivers')
plt.xlabel('Distance Feature')
plt.ylabel('Speeding Feature')
plt.legend()
plt.show()


# Fitting K-Means to the dataset (for Rash and Safe Drivers)
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
cluster_pred = kmeans.fit_predict(features)

# Visualising the clusters
plt.scatter(features[cluster_pred == 0, 0], features[cluster_pred == 0, 1], s = 100, c = 'red', label = 'Rural Safe Drivers')
plt.scatter(features[cluster_pred == 1, 0], features[cluster_pred == 1, 1], s = 100, c = 'blue', label = 'Urban Safe Drivers')
plt.scatter(features[cluster_pred == 2, 0], features[cluster_pred == 2, 1], s = 100, c = 'green', label = 'Urban Rash Drivers')
plt.scatter(features[cluster_pred == 3, 0], features[cluster_pred == 3, 1], s = 100, c = 'cyan', label = 'Rural Rash Drivers')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of Drivers')
plt.xlabel('Distance Feature')
plt.ylabel('Speeding Feature')
plt.legend()
plt.show()