# k-fold cross validation
# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing the dataset
dataset = pd.read_csv('Social_Network_Ads_2.csv')
dataset.shape
dataset.columns.tolist()

# separating out features and labels
features = dataset.iloc[:,[2,3]].values
labels = dataset.iloc[:,4].values

# train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels,
                                                    test_size=0.25,random_state=0)

# feature scaling/normalisation
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# fitting knn to training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(features_train,labels_train)

# predicting the test results
labels_pred = classifier.predict(features_test)

# making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

# applying k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier,X = features_train, y = labels_train, cv = 10)
print ("accuracies is ", accuracies)
print ("mean accuracy is",accuracies.mean())

# Visualising the Training set results
# Plot the decision boundary. For that, we will assign a color to each


# Step 1 is to find the minimum and maximum of x and y 
# 0th column is the x values
x_min = features_train[:, 0].min() - 1
x_max = features_train[:, 0].max() + 1
print(x_min)
print(x_max)


# 1st column is the y values
y_min = features_train[:, 1].min() - 1
y_max = features_train[:, 1].max() + 1
print(y_min)
print(y_max)

# Minimum values are in negative and maximum values are positive

# Step 2
# We want to generate more points between these range only
# We need to give minimum and maximum and the difference 
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

print(xx.shape)
print(yy.shape)

# x set of values are in xx
# y set of values are in yy

# If v open and check, there is a pattern, 
# x axis values are changing since y = 0
print(xx)


# If v open and check, there is a pattern, 
# y axis values are changing since x = 0
print(yy)


# We need to take x values from first row of xx 
# and y values from the first row of yy 
# These two will make the points
# We want to predict for each points generated for drawing the decission boundary
# For prediction method i need to pass them as one set

# We need to flatten all the data of xx, that will come in one column
# 2D to 1D
xt = xx.ravel()
print(xt.shape)   # 60x62 = 3720
print(xt)

# Then we need to flatten all the data of yy, that will come in one column
# 2D to 1D
yt = yy.ravel()
print(yt.shape)   # 60x62 = 3720
print(yt)


# Need to make them as points now, similar to zip
pt = np.c_[xt,yt]   # similar to pt = zip(xt,yt) or np.concatenate
print(pt.shape)
print(pt)

# To draw the decission boundary need to get the prediction
# whether it belongs to which category
# xx yy and Z should have the same shape, so we have to reshape it
Z = classifier.predict(pt)
print(Z.shape)


# We have to reshape the Z as xx and yy 
Z = Z.reshape(xx.shape)
print(Z.shape)
# Z stores the prediction wiht only 2 class 


# Now we need to plot xx , yy and Z, all 3 combination 
# Its a 3D data, but we plot only 2D data in matplotlib
# How to show 3D data into 2D ?
# We can use 2 colors and show one set of xx and yy in GREEN which has Z = 0
# and in RED which has Z = 1
# Such things are known as contours

# we are trying to plot a 3D data now, since we have xx, yy and Z also
# How to show 3D data into 2D form
# So we can use the color to represent the Z value

# Open contour_plot.png

"""
A contour plot is a graph that you can use to explore the potential 
relationship between three variables. 
Contour plots display the 3-dimensional relationship 
in two dimensions, with x- and y-factors (predictors) plotted on the 
x- and y-scales and response values represented by contours.
""" 


#plot the decission boundary
plt.contourf(xx, yy, Z, alpha=1.0)



# I have to overlays the points
# Plot the points

# class = 0 and x coordinate so 0 and y coordinate so 1
plt.plot(features_test[labels_test == 0, 0], features_test[labels_test == 0, 1], 'ro', label='Class 1')


# class = 1 and x coordinate so 0 and y coordinate so 1
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'bo', label='Class 2')


# U can see from the visual and compare it with cm, that 4 points were different
# and similarly for 3 points 
plt.show()
print(cm)