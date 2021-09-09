# Automobile

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile.csv')

df.columns

df.isnull().any(axis = 0)

df[df.isnull().any(axis = 1)]

#  Handle the missing values for Price column
df['price'].mean()  #13207.129353233831
df['price'] = df['price'].fillna(df['price'].mean())

#Get the values from Price column into a numpy.ndarray
type(df)
df
x = df['price'].values

# Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
df['price'].min()
# 5118.0
df['price'].max()
# 45400.0
df['price'].mean()
# 13207.129353233831
df['price'].std()
# 7868.768212343796

# Pie-chart
series = df["make"].value_counts()

topCarMakers = series.index[0:11]
vehicleCount = series.values[0:11]

plt.pie(vehicleCount, labels=topCarMakers, autopct='%.2f%%')

plt.show()
