# use of numpy and matplotlib

# multiplying each item in a list by 10
list2 = []
list1 = [1,2,3,4,5,6]
for item in list1:
    list2.append(item*10)

# list comprehension
[item**3 for item in list1]


list1 = [1,2,3,4,5,6]
import numpy as np
x = np.array(list1)
x.shape
x.ndim

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.scatter(x, y)
plt.plot(x,y)

x = np.arange(20)
y = [item**3 for item in x]
plt.scatter(x, y)
plt.plot(x,y)

branchnames = ['CSE','IT','ECE','EE']
sizes = [10,5,5,2]
apart = (0,0,0.1,0)
plt.pie(sizes, explode=apart ,labels=branchnames, autopct='%.2f%%')

plt.show()