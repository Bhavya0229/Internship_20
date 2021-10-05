"""
Data Source File: deliveryfleet.csv

In this code challenge we need two driver features: 
mean distance driven per day (Distance_Feature) 
and 
the mean percentage of time a driver was > 5 mph over the 
speed limit (Speeding_Feature).

Perform Dbscan clustering to distinguish urban drivers 
and rural drivers. Further distinguish 
speeding drivers from those who follow speed limits.

Label accordingly for the 4 groups.
"""

# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# importing the dataset
dataset = pd.read_csv('deliveryfleet.csv')
dataset.columns.tolist()

# extracting out features
features = dataset.iloc[:,[1,2]].values

# scatter all the points
plt.scatter(features[:,0],features[:,1])
plt.plot()

# feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler().fit(dataset)
dataset = sc.transform(dataset)

# compute dbscan
from sklearn.cluster import DBSCAN
db = DBSCAN(eps = 0.3, min_samples=10).fit(dataset)
labels_pred = db.labels_ # belongs to which cluster id
print(labels_pred)

len(features[labels_pred == 0])
len(features[labels_pred == 1])

len(features[labels_pred == 2])

len(features[labels_pred == -1])

plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+', label = 'Rural Overspeed'  )
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o', label = 'Rural Safe Driver'  )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s', label = 'Urban Safe Driver'  )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*', label = 'outliers' )

plt.title('Clusters of Drivers')
plt.xlabel('Distance_Feature')
plt.ylabel('Speed_Feature')
plt.legend()
plt.show()