# Thanks Giving

import pandas as pd
import numpy as np
import re

df = pd.read_csv('thanksgiving.csv', encoding ='Windows 1252')

# Fetching the columns name for further reference
col_df = df.columns.tolist()

# Initializing a code number for each column name
thanksgiving_col = [x for x in range(0,65)]

# Storing the column name with their codes for further reference
col_name = dict(zip(thanksgiving_col, col_df))

# Initializing the dataframe with the codes of the column
df.columns = thanksgiving_col


# Fetch the data of the people who perform thanksgiving.
thanksgiving_df= df[df[1] == 'Yes']

#check for missing values
missing_val = df[df.isnull().any(axis = 1)]

# Fill out the nan values with 'Missing' keyword
df = df.replace(np.nan,'Missing')

#Analyse for the state, area  and income based what is consumed in 
#thankgiving dinner

df[60]
df[64]
df[3]
region_based = df.groupby(64)
print(region_based.groups)
print(region_based.size())

income_based = df.groupby(63)
print(income_based.groups)
print(income_based.size())

area_based = df.groupby(60)
print(area_based.groups)
print(area_based.size())
    
# Analysis of the sauces prefered by each incomes group people
sauces_pref = df.groupby(8)[63].value_counts()
print(sauces_pref)

# What is your gender? convert column to numeric values. 
# We’ll assign 0 to Male, and 1 to Female.
def gender(value):
    if value == 'Male':
        value = 0
    elif value == 'Female':
        value = 1
    return value
df[62] = df[62].apply(gender)
print(df[62].value_counts(dropna = False))

#income cleanup
df[63] = df[63].replace(['Prefer not to answer','Missing'],['0','0'])
regex = re.compile("\d+\W*\d+")
# A function to be passed in .apply() method for filtering out the salaries
def income_filter(value):
    value = regex.findall(value)
    value = [int(x.replace(",", "")) for x in value]
    return sum(value)/(len(value)+0.1)

# Using the apply method to filter the income column
df[63] = df[63].apply(income_filter)

# Fetching the average incomes for each type sauces
avg_income_sauce = df.groupby(8)[63]
print(avg_income_sauce.groups)
avg_income_sauce = avg_income_sauce.mean()
print(avg_income_sauce)

# Visualizing the average income of the various sauces
avg_income_sauce.plot.bar()


