#creating bakeryDB.sqlite database

import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'csuDB.sqlite' )

# 02.   import data from different csv files
df = pd.read_csv('csufees.csv', delimiter=(','))
df.to_sql('csufees', conn,  if_exists='append', index=False)
df = pd.read_csv('Campuses.csv', delimiter=(','))
df.to_sql('Campuses', conn,  if_exists='append', index=False)
df = pd.read_csv('disciplines.csv', delimiter=(','))
df.to_sql('disciplines', conn,  if_exists='append', index=False)
df = pd.read_csv('discipline_name.csv', delimiter=(','))
df.to_sql('discipline_name', conn,  if_exists='append', index=False) 


# 03.   creating cursor to use csuDB   
c = conn.cursor()
print(c.description)

# Report all campuses from Los Angeles county. Output the full name of 
#campus in alphabetical order.
c.execute("""SELECT Campus,county FROM Campuses WHERE County LIKE '%Los Angeles%'
          ORDER BY Campus""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Campus","County"]
print(df)

#For each year between 1994 and 2004 (inclusive) report the number of students who
#enrolled for undergraduate from California Maritime Academy Output the year,no. of enrollments for each year.
c.execute("""select Campuses.Campus, Disciplines.Year, sum(Disciplines.Undergraduate) as sum_undergraduate
               from Disciplines, Campuses
               where 
               Disciplines.Year between 1994 AND 2004 AND
               Campuses.Campus like "%California  Maritime Academy%" AND
               Disciplines.Campus=Campuses.Id
               group by
               Disciplines.Year
               order by sum_undergraduate""")
for i in c.fetchall():
    print(i)
print()

#Report undergraduate and graduate enrollments (as two numbers) in 'Mathematics', 'Engineering' and 'Computer'.
c.execute("""SELECT SUM(disciplines.Undergraduate) AS sum_ug,SUM(disciplines.Graduate) AS sum_g,discipline_name.Name 
          FROM disciplines,discipline_name
          WHERE (disciplines.Discipline = discipline_name.Id) AND
          discipline_name.Name IN('Mathematics','Engineering','Computer and Info. Sciences')
          GROUP BY discipline_name.Name""")
df = pd.DataFrame(c.fetchall())
df.columns = ["sum_ug","sum_g","Name"]
print(df)

# Report graduate enrollments in 2004
#Report only one row from each university the number of graduate students.
c.execute("""SELECT SUM(disciplines.Graduate) AS sum_g,disciplines.Year,disciplines.Campus 
          FROM disciplines
          WHERE disciplines.Year=2004 GROUP BY disciplines.Campus""")
df = pd.DataFrame(c.fetchall())
df.columns = ["sum_g","Year","Campus"]
print(df)

# Find all  campuses where graduate enrollment in 2004 was at least double than undergraduate 
#Report campus names and discipline id. 
#Sort output by campus name in alphabetical order.
c.execute("""SELECT Campuses.Campus,disciplines.Discipline
          FROM disciplines,Campuses WHERE (disciplines.Campus = Campuses.Id) AND
          (disciplines.Graduate >= 2*disciplines.Undergraduate)
          AND disciplines.Year = 2004
          ORDER BY Campuses.Campus""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Campus","Id"]
print(df)

#Report the total amount of money collected from student fees at ’Fresno State University’ 
#for each year between 2002 and 2004 inclusively,. Output the year.
c.execute("""SELECT SUM(CampusFee) AS total_fee,csufees.Year,Campuses.Campus
          FROM csufees,Campuses WHERE (csufees.Campus = Campuses.Id)
          AND (Campuses.Campus LIKE '%Fresno State University%')
          AND (csufees.Year BETWEEN 2002 AND 2004)
          GROUP BY csufees.Year""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_fee","Year","Campus"]
print(df)

#Find all campuses where enrollment in 2004 , was higher than the 2004 enrollment 
#in 'San Jose State University'.
#Report the name of campus.
c.execute("""SELECT Campuses.Campus,SUM(disciplines.Undergraduate+disciplines.Graduate) AS 
          total_enrl FROM Campuses,disciplines
          WHERE (disciplines.Campus = Campuses.Id) AND
          (Campuses.Campus LIKE '%San Jose State University%')
          AND disciplines.Year = 2004""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_fee","Year","Campus"]
print(df)
