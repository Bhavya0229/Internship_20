#creating bakeryDB.sqlite database

import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'bakeryDB.sqlite' )

# 02.   import data from bakery.csv
df = pd.read_csv('bakery.csv', delimiter=(';'))
df.to_sql('bakery', conn,  if_exists='replace', index=False) 

# 03.   creating cursor to use bakeryDB    
c = conn.cursor()
print(c.description)

#Display How many Chocolate Flavoured Foods are there in bakery table ?
c.execute("""SELECT COUNT(bakery.Flavor) AS total_chocolates,Food,Flavor
          FROM bakery WHERE Flavor = 'Chocolate' GROUP BY Food""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_chocolates","Food","Flavor"]
print(df)

#Display the total price of Foods which are Apple Flavoured from bakery table ?
c.execute("""SELECT SUM(bakery.Price) AS total_price,Flavor
          FROM bakery WHERE Flavor = 'Apple'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_price","Flavor"]
print(df)

# Display average amount of cake Flavoured Foods from bakery table ?
c.execute("""SELECT AVG(bakery.Price) AS avg_price,Food,Flavor
          FROM bakery WHERE Food = 'Cake' GROUP BY Flavor""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_price","Food","Flavor"]
print(df)

#Display the maximum price from bakery table ?
c.execute("""SELECT Max(Price) AS max_price
          FROM bakery""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_price"]
print(df)

#Display the minimum price from bakery table ?
c.execute("""SELECT Min(Price) AS max_price
          FROM bakery""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_price"]
print(df)

#Display count of every Food from bakery table ?
c.execute("""SELECT COUNT(bakery.Food) AS total_foods,Food
          FROM bakery GROUP BY Food""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_foods","Food"]
print(df)

#Display the total price of Each Flavour from bakery table  ?
c.execute("""SELECT SUM(bakery.Price) AS total_price,Flavor
          FROM bakery GROUP BY Flavor""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_price","Flavor"]
print(df)

#Display average price for Cake or Eclair from bakery table ?
c.execute("""SELECT AVG(bakery.Price) AS avg_price,Food
          FROM bakery WHERE Food = 'Cake'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_price","Food"]
print(df)

c.execute("""SELECT AVG(bakery.Price) AS avg_price,Food
          FROM bakery WHERE Food = 'Eclair'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_price","Food"]
print(df)

#Display the maximum price of each Food from bakery table ?
c.execute("""SELECT Max(bakery.Price) AS max_price,Food
          FROM bakery GROUP BY FOOD""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_price","Food"]
print(df)

#Display the minimum price of each Flavour from bakery table ?
c.execute("""SELECT MIN(bakery.Price) AS min_price,Flavor
          FROM bakery GROUP BY Flavor""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_price","Flavor"]
print(df)

#Display count of every Food from bakery table and sort them by count ?
c.execute("""SELECT COUNT(bakery.Food) AS total_foods,Food
          FROM bakery GROUP BY FOOD ORDER BY total_foods""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_foods","Food"]
print(df)

#Display the total price of each Flavour from bakery table and sort them by price ?
c.execute("""SELECT SUM(bakery.Price) AS total_price,Flavor
          FROM bakery GROUP BY Flavor ORDER BY Price""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_price","Flavor"]
print(df)

# Display average price for each Food from bakery table and sort them by average price ?
c.execute("""SELECT AVG(bakery.Price) AS avg_price,Food
          FROM bakery GROUP BY Food ORDER BY avg_price""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_price","Food"]
print(df)

# Display the maximum price of each Food from bakery table and sort them by maximum price ?
c.execute("""SELECT Max(bakery.Price) AS max_price,Food
          FROM bakery GROUP BY FOOD ORDER BY max_price""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_price","Food"]
print(df)

# Display the minimum price of each Flavour from bakery table and sort them by minimum price ?
c.execute("""SELECT MIN(bakery.Price) AS min_price,Flavor
          FROM bakery GROUP BY Flavor ORDER BY min_price""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_price","Flavor"]
print(df)

# Display count of every Food from bakery table in descending order ?
c.execute("""SELECT COUNT(bakery.Food) AS total_foods,Food
          FROM bakery GROUP BY FOOD ORDER BY total_foods DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_foods","Food"]
print(df)

# Display the total price of each Flavour from bakery table in descending order ?
c.execute("""SELECT SUM(bakery.Price) AS total_price,Flavor
          FROM bakery GROUP BY Flavor ORDER BY total_price DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_price","Flavor"]
print(df)

#Display average price for each Food from bakery table in descending order ?
c.execute("""SELECT AVG(bakery.Price) AS avg_price,Food
          FROM bakery GROUP BY Food ORDER BY avg_price DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_price","Food"]
print(df)

#Display the maximum price for each food from bakery table in descending order ?
c.execute("""SELECT Max(bakery.Price) AS max_price,Food
          FROM bakery GROUP BY FOOD ORDER BY max_price DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_price","Food"]
print(df)

# Display the minimum price for each food from bakery table in descending order ?
c.execute("""SELECT MIN(bakery.Price) AS min_price,Food
          FROM bakery GROUP BY Food ORDER BY min_price DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_price","Food"]
print(df)

#  Display Flavour column from bakery table without duplicates ?
c.execute("""SELECT DISTINCT(Flavor) FROM BAKERY""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Flavor"]
print(df)

#Display count of each Food, which have Chocolate Flavour , also arrange food's name in alphabetical order ?
c.execute("""SELECT COUNT(bakery.Food) AS total_foods,Food
          FROM bakery WHERE Flavor = 'Chocolate' GROUP BY FOOD ORDER BY Food""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_foods","Food"]
print(df)