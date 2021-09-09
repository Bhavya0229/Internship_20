# cars 
import pandas as pd

df = pd.read_csv('cars.csv')
df.columns.tolist()

from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(df, test_size= 0.5, random_state=0)

df_train.to_csv('df_train.csv',index = False)
df_test.to_csv('df_test.csv',index = False)

