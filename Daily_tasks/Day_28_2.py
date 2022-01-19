# apriori algorithm

# importing the libraries
import pandas as pd
from apyori import apriori

# Data Preprocessing
# Column names of the first row is missing, header - None
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)
print(type(rules))


"""
Shortcut to write a generator

q = (i**2 for i in [1,2,3,4,5])
print(type(q))
next(q)
p = list(q)
print(p)
"""

# Visualising the results
results = list(rules)
print(len(results))

results[0].items
results[0].support
results[0][2]

