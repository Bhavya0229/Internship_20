# sqlite3 code challenge 2

#creating reservationsDB.sqlite database

import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'reservationsDB.sqlite' )

# import data from reservations.csv 
df = pd.read_csv('reservations.csv', delimiter=(','))
df.to_sql('reservations', conn,  if_exists='replace', index=False) 

# creating cursor to use reservationsDB
c = conn.cursor()
print(c.description)

# Display all columns data of all the rows from the RESERVATIONS table ?
c.execute("""SELECT * 
          FROM reservations""")
print(c.description)
df = pd.DataFrame(c.fetchall())
df.columns = ["Code","Room","CheckIn","CheckOut","Rate","FirstName",
              "LastName","Adults","Childs"]
print(df)

#Display FirstName and LastName of all the guests from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName 
          FROM reservations""")
print(c.description)
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName",
              "LastName"]
print(df)

# Display first name of all the guests from the RESERVATIONS table ?
c.execute("""SELECT FirstName 
          FROM reservations""")
print(c.description)
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName"]
print(df)

# Select all guests, that have Adults 2 from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName,Adults 
          FROM reservations WHERE Adults = 2""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Adults"]
print(df)

#Select all guests, that have Childs 1 from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName,Childs 
          FROM reservations WHERE Childs = 1""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Childs"]
print(df)

# Select all the guests, that have not Adults 0 from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName,Adults 
          FROM reservations WHERE Adults != 0""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Adults"]
print(df)

# Select all the guests for whom Rate is more than 150.0 from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName,Adults 
          FROM reservations WHERE Rate>150""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Rate"]
print(df)

#Select all guests whose FirstName contains at least one a character from the RESERVATIONS table ?
c.execute("""SELECT FirstName 
          FROM reservations WHERE FirstName LIKE'%a%'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName"]
print(df)

# Select all guests whose LastName starts with ‘m’  from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName 
          FROM reservations WHERE LastName LIKE'm%'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName"]
print(df)

# Select all guests whose FirstName is exactly five characters long from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName 
          FROM reservations WHERE FirstName LIKE'_____'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName"]
print(df)

# Select only those guests from the RESERVATIONS table that: have a FirstName exactly five characters long, have a Adults more than 2
c.execute("""SELECT FirstName,LastName,Adults 
          FROM reservations WHERE FirstName LIKE'_____' AND Adults > 2""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Adults"]
print(df)

# Select guests that have 2 Adults with Room Rent 250.0 from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName,Adults,Rate 
          FROM reservations WHERE Adults = 2 AND Rate = 250""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Adults","Rate"]
print(df)

# Select all the guests whose CheckIn is any of these: 01-jan-10, 01-feb-10, 01-mar-10, 01-apr-10, 01-may-10 from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName,CheckIn 
          FROM reservations WHERE CheckIn IN("01-JAN-10", "01-FEB-10", "01-MAR-10", "01-APR-10", "01-MAY-10")""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","CheckIn"]
print(df)

# Select all the CheckIn that are not in jan month from the RESERVATIONS table ?
c.execute("""SELECT FirstName,LastName,CheckIn 
          FROM reservations WHERE CheckIn NOT LIKE '%JAN%'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","CheckIn"]
print(df)

# Select all the guests where CheckOut is null?
c.execute("""SELECT FirstName,LastName,CheckIn 
          FROM reservations WHERE CheckIn LIKE 'NULL'""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","CheckIn"]
print(df)

# Select all the guests where Rate is between 200 to 250?
c.execute("""SELECT FirstName,LastName,Rate 
          FROM reservations WHERE Rate BETWEEN 200 AND 250""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Rate"]
print(df)

# sort all the guests according to their Rate.
c.execute("""SELECT FirstName,LastName,Rate 
          FROM reservations ORDER BY Rate""")
df = pd.DataFrame(c.fetchall())
df.columns = ["FirstName","LastName","Rate"]
print(df)

#Delete the table
c.execute("""DROP TABLE bakery""")
conn.commit()

conn.close()