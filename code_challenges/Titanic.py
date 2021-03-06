# EDA with Titanic.csv

import pandas as pd

df = pd.read_csv('titanic.csv')

df.columns

# How many people survived the disaster ?

people_survived = df['Survived'].value_counts()[1]
print(str(people_survived) + " People Survived")
# 342 People Survived


# How many people died ?
people_died = df['Survived'].value_counts()[0]
print(str(people_died) + " People Died")
# 549 People Died

# Calculate the survival rates as proportions (percentage)
disaster_survived_percentage = df['Survived'].value_counts(normalize=True)[1]
print(str(round(float(disaster_survived_percentage)*100,2)) + "% People Survived")
# 38.38% People Survived

disaster_died_percentage = df['Survived'].value_counts(normalize=True)[0]
print(str(round(float(disaster_died_percentage)*100,2)) + "% People Died")
# 61.62% People Died

# Males that survived vs males that passed away
male_survived = df['Survived'][df['Sex'] == 'male'].value_counts(normalize=True)[1]
male_passed_away =  df['Survived'][df['Sex'] == 'male'].value_counts(normalize=True)[0]
print ("male_survived : "+str(round(male_survived*100,2))+"%")
print ("male_passed_away : "+str(round(male_passed_away*100,2))+"%")
# male_survived : 18.89%
# male_passed_away : 81.11%

# Females that survived vs Females that passed away 
female_survived = df['Survived'][df['Sex'] == 'female'].value_counts(normalize=True)[1]
female_passed_away =  df['Survived'][df['Sex'] == 'female'].value_counts(normalize=True)[0]
print ("female_survived : "+str(round(female_survived*100,2))+"%")
print ("female_passed_away : "+str(round(female_passed_away*100,2))+"%")
# female_survived : 74.2%
# female_passed_away : 25.8%

# Does age play a role?
def filter_data(value):
    if 0 <= value <= 18:
        return 1
    else:
        return 0


df['Child'] = df['Age'].apply(filter_data)
c =  df['Survived'][df['Child'] == 1].value_counts(normalize=True)
print ("Child Survived : "+str(round(c[1]*100, 2))+"%")
# Child Survived : 50.36%










