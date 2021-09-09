# EDA_bitly
import pandas as pd
import numpy as np

bitly_df = pd.read_json('bitly.json',lines = True)
#Replace the 'nan' values with 'Missing' and ' ' values with 'Unknown' keywords
bitly_df.isnull().any(axis = 0)
bitly_df = bitly_df.replace(np.nan,'Missing')
bitly_df = bitly_df.replace('','Unknown')
bitly_df.columns.tolist()

#task 02: Print top 10 most frequent time-zones from the Dataset
bitly_values = bitly_df['tz'].value_counts()[0:10]

#task 03: Count the number of occurrence for each time-zone
bitly_count = bitly_df['tz'].value_counts()

#task 04: Plot a bar Graph to show the frequency of top 10 time-zones
bitly_values.plot.bar()

# From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
tokens_df = bitly_df['a'].str.split(n = 1, expand = True).add_prefix("Token_")

#Fetching the frequency of the browser capability
token_frequency = tokens_df['Token_0'].value_counts()

# Plotting bar graph for top 5 browser capability
token_frequency[0:5].plot(kind='bar')

# Filling the missing values in the token parts with mising string
tokens_df = tokens_df.replace(np.nan,'Missing')

#task 06:

# Classifying as windows os and non-windows os

# Initializing the os column as Not windows
tokens_df['Os'] = 'Not Windows'
tokens_df["Os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"

