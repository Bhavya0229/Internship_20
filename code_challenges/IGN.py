# IGN Analysis

import pandas as pd

df = pd.read_csv('ign.csv')

df.columns.tolist()
df['score']
df['platform']

# we want to find games released for the Xbox One that have a score of more than 7.
games = df[(df['platform'] == 'Xbox One') & (df['score'] > 7)]
games_released = games['title']
print(games_released)

# review distribution for the Xbox One vs the review distribution 
# for the PlayStation

import matplotlib.pyplot as plt
xbox_one = df['platform']=="Xbox One"
xbox_one_only_df = df[xbox_one]
xbox_one_reviews = xbox_one_only_df['score_phrase']
xbox_one_reviews.hist(bins=20, grid=False, xrot=90)

# review distribution for the PlayStation 4
ps4 = df['platform']=="PlayStation 4"
ps4_only_df = df[ps4]
ps4_reviews = ps4_only_df['score_phrase']
ps4_reviews.hist(bins=20, grid=False, xrot=90)

