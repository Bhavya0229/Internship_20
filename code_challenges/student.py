# creating studentDB.sqlite database

import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'studentDB.sqlite' )

# import data from student.csv 
df = pd.read_csv('student.csv', delimiter=(','))
df.to_sql('student', conn,  if_exists='replace', index=False) 

#creating cursor to use studentDB    
c = conn.cursor()
print(c.description)

#Display How many students are there in student table ?
c.execute("""SELECT COUNT(student.StFirstName) AS total_st FROM student""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_st"]
print(df)

# Display the average grade of students from student table ?
c.execute("""SELECT AVG(student.Grade) AS avg_grade FROM student""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_grade"]
print(df)

# Display the maximum grade from student table ?
c.execute("""SELECT MAX(student.Grade) AS max_grade FROM student""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_grade"]
print(df)

#Display the minimum grade from student table ?
c.execute("""SELECT MIN(student.Grade) AS min_grade FROM student""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_grade"]
print(df)

# Display the count of students for each grade from student table ?
c.execute("""SELECT COUNT(student.StFirstName) AS total_st,Grade FROM student
          GROUP BY Grade""")
df = pd.DataFrame(c.fetchall())
df.columns = ["total_st","Grade"]
print(df)

# Display average grade for classroom 101 or 102 from student table ?
c.execute("""SELECT AVG(student.Grade) AS avg_grade,Classroom FROM student
          WHERE Classroom = 101""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_grade","Classroom"]
print(df)

c.execute("""SELECT AVG(student.Grade) AS avg_grade,Classroom FROM student
          WHERE Classroom = 102""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_grade","Classroom"]
print(df)

#Display the maximum grade of each classroom from student table ?
c.execute("""SELECT MAX(student.Grade) AS max_grade,Classroom FROM student 
          GROUP BY Classroom""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_grade","Classroom"]
print(df)

# Display the minimum grade of each classroom from student table ?
c.execute("""SELECT MIN(student.Grade) AS min_grade,Classroom FROM student 
          GROUP BY Classroom""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_grade","Classroom"]
print(df)

# Display count of every classroom from student table and sort them by count ?
c.execute("""SELECT COUNT(student.Classroom) AS st_count,Classroom FROM student 
          GROUP BY Classroom ORDER BY st_count""")
df = pd.DataFrame(c.fetchall())
df.columns = ["st_count","Classroom"]
print(df)

# Display average grade for each classroom from student table in descending order ?
c.execute("""SELECT AVG(student.Grade) AS avg_grade,Classroom FROM student
          GROUP BY Classroom ORDER BY avg_grade DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["avg_grade","Classroom"]
print(df)

# Display the maximum grade of each classroom from student table and sort them by maximum grade ?
c.execute("""SELECT MAX(student.Grade) AS max_grade,Classroom FROM student 
          GROUP BY Classroom ORDER BY max_grade""")
df = pd.DataFrame(c.fetchall())
df.columns = ["max_grade","Classroom"]
print(df)

# Display the minimum grade of each classroom from student table in descending order ?
c.execute("""SELECT MIN(student.Grade) AS min_grade,Classroom FROM student 
          GROUP BY Classroom ORDER BY min_grade DESC""")
df = pd.DataFrame(c.fetchall())
df.columns = ["min_grade","Classroom"]
print(df)

#Display the grade, Firstname, Secondname and classroom of top 3 students according to their grade from student table ?
c.execute("""SELECT StLastName,StFirstName,Grade,Classroom FROM student
          GROUP BY Grade
          LIMIT 3""")
df = pd.DataFrame(c.fetchall())
df.columns = ["StLastName","StFirstName","Grade","Classroom"]
print(df)