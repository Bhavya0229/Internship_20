"""
Import Crime.csv File.
    Perform dimension reduction and group the cities using k-means based on 
    Rape, Murder and assault predictors.
"""
# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# importing the dataset
dataset = pd.read_csv('crime_data.csv')

dataset.isnull().any(axis = 0)

features = dataset.iloc[:,[1,2,4]].values

# feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
features = pca.fit_transform(features)

# visualizing the data
plt.scatter(features[:,0],features[:,1])
plt.show()

# How much is the loss and how much we are able to retain the information
explained_variance = pca.explained_variance_ratio_
print(explained_variance)
# first paramater (PC1) is holding 78% of the 3D data
# second parameter (PC2) is holding 15% of the 3D data

# elbow method
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)  # we have not used the fit_predict
    wcss.append(kmeans.inertia_)
print(wcss)

# plot wcss
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# fitting the model
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4,init ='k-means++', random_state=0)
pred_cluster = kmeans.fit_predict(features)
print(pred_cluster)

#new add column
dataset["pred_cluster"] = pred_cluster


# visualizing the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'purple', label = 'Cluster 4')

# finding the centroid
print(kmeans.cluster_centers_)
print(kmeans.cluster_centers_[:, 0]) # x 
print(kmeans.cluster_centers_[:, 1]) # y 

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'purple', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()

# states with cluster id =0
dataset[pred_cluster == 0]

# states with cluster id =1
dataset[pred_cluster == 1]

# states with cluster id =2
dataset[pred_cluster == 2]

# states with cluster id =3
dataset[pred_cluster == 3]