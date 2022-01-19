# Data analytics with pandas

import pandas as pd

df = pd.read_csv('Salaries.csv')

df.head

df.columns.tolist()

df['salary']

# entries whose salaries is greater than 100000
df['salary'] > 100000

df[df['salary'] > 100000]

df[(df['salary'] > 100000) & (df['sex'] == 'Female')]

df.isnull().any(axis = 0)

df[df.isnull().any(axis = 1)]

df['phd'].mean()
df['phd'] = df['phd'].fillna(df['phd'].mean())

df2 = df.fillna(100)

df.dropna(inplace = True)

df = pd.read_csv('Salaries.csv')

df.iloc[0:10,2:4]

df.iloc[10, : ]
df.iloc[[10,15], : ]
df.iloc[:,2]
