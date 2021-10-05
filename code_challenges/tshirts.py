"""

T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height 
and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. 
How would you figure out the actual size of these 3 types of shirt to better 
fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of 
the data as stated above.
"""

# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# importing the dataset
dataset = pd.read_csv('tshirts.csv')
dataset.columns.tolist()
dataset.head(10)
dataset.isnull().any(axis = 0)

# separating out features 
features = dataset.iloc[:,[1,2]].values

# visualising the data
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

# plot wcss
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# fitting the model
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3,init ='k-means++', random_state=0)
pred_cluster = kmeans.fit_predict(features)
print(pred_cluster)

# visualizing the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1],s = 100, c = 'blue', label = 'Medium')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1],s = 100, c = 'red', label = 'Large')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1],s = 100, c = 'green', label = 'Small')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],s = 200, c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Height(inches)')
plt.ylabel('Weight(pounds)')
plt.legend()
plt.show()