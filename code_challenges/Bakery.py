# sqlite3 code challenge 1

# 1. creating bakeryDB.sqlite database

import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'bakeryDB.sqlite' )

# 02.   import data from bakery.csv
df = pd.read_csv('bakery.csv', delimiter=(';'))
df.to_sql('bakery', conn,  if_exists='replace', index=False) 

# 03.   creating cursor to use bakeryDB    
c = conn.cursor()
print(c.description)

# 04. Display all columns data of all the rows from the bakery table ?
c.execute("""SELECT * 
          FROM bakery""")
print(c.description)
df = pd.DataFrame(c.fetchall())
df.columns = ["Id","Flavour","Food","Price"]
print(df)

# 05.   Display goods and their price code from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

# 06.   Display all goods from bakery table ?
c.execute("""SELECT  Food
          FROM bakery""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food"]
print(df)

# 07.   Select all goods whose price is 3.25 from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price = 3.25""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

# 08.   Select all goods whose price is 3.25 or 8.95 from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price IN(3.25,8.95)""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

# 09.   Select all goods who price is not 3.25 or 8.95 from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price NOT IN(3.25,8.95)""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

#10.   Select all goods whose price is greater than 3 from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price > 3""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

#11.   Select all goods names where first letter c from bakery table ?
c.execute("""SELECT  Food
          FROM bakery WHERE Food LIKE 'c%'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food"]
print(df)

#12.   Select all goods whose food name ends  with rt from bakery table ?
c.execute("""SELECT  Food
          FROM bakery WHERE Food LIKE '%rt'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food"]
print(df)

#13.   Select all goods names which having exactly 4 characters from bakery table ?
c.execute("""SELECT  Food
          FROM bakery WHERE Food LIKE '____'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food"]
print(df)

# 14.   Select all goods names who has price greater than 3 or who ends with ke from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price>3 OR Food LIKE '%ke'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

#15.   Select all goods whose price are 3.25,8.95,3.75 from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price IN(3.25,8.95,3.75)""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

#16.   Select all the goods names that are not 4 characters long from bakery table ?
c.execute("""SELECT  Food
          FROM bakery WHERE Food NOT LIKE '____'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food"]
print(df)

# 17.   Select all goods where price is null?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price IS NULL""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

# 18.   Select all goods whose price code between 3.25 and 8.95 from bakery table ?
c.execute("""SELECT  Food,Price
          FROM bakery WHERE Price BETWEEN 3.25 AND 8.95""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

#19.   Sort bakery table with their price code?
c.execute("""SELECT  Food,Price
          FROM bakery ORDER BY Price""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Food","Price"]
print(df)

#Delete the table
c.execute("""DROP TABLE bakery""")
conn.commit()




conn.close()