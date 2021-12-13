# creating innDB.sqlite database
import sqlite3
import pandas as pd

conn = sqlite3.connect ( 'innDB.sqlite' )

#import data from Reservations.csv, Rooms.csv 
df = pd.read_csv('reservations.csv', delimiter=(','))
df.to_sql('reservations', conn,  if_exists='append', index=False)
df = pd.read_csv('Rooms.csv', delimiter=(','))
df.to_sql('Rooms', conn,  if_exists='append', index=False)

#creating cursor to use innDB
c = conn.cursor()

# Find all modern rooms with a base price below $160 and two beds.Report 
#room names and codes in alphabetical order by the code.

c.execute("""SELECT Rooms.roomName,reservations.Code FROM Rooms,reservations
          WHERE (reservations.Room = Rooms.RoomId) 
          AND (Rooms.decor LIKE '%modern%')
          AND (Rooms.basePrice<160)
          AND (Rooms.beds = 2)
          ORDER BY reservations.Code""")
df = pd.DataFrame(c.fetchall())
df.columns = ["roomName","Code"]
print(df)

#Find all July reservations for the ’Convoke and sanguine’ room. For each reservation
#report the last name of the person who reserved it, checkin and checkout dates, 
#the total number of people staying and the daily rate.
#Output reservations in chronological order.
c.execute("""SELECT reservations.LastName,reservations.CheckIn,reservations.CheckOut,
          (reservations.Adults+reservations.Kids) AS total_ppl,reservations.Rate
          FROM reservations,Rooms WHERE (reservations.Room = Rooms.RoomId)
          AND (reservations.CheckIn LIKE '%JUL%')
          AND (Rooms.roomName LIKE '%Convoke and sanguine%')
          ORDER BY total_ppl""")
df = pd.DataFrame(c.fetchall())
df.columns = ["LastName","CheckIn","CheckOut","total_ppl","Rate"]
print(df)

#Find all rooms occupied on February 6, 2010. Report full 
#name of the room, the check-in and checkout dates of 
#the reservation. Sort output in alphabetical order by room name.
c.execute("""SELECT Rooms.roomName,reservations.CheckIn,reservations.CheckOut
          FROM reservations,Rooms WHERE (reservations.CheckOut LIKE '%06-FEB-10%')
          ORDER BY Rooms.roomName""")
df = pd.DataFrame(c.fetchall())
df.columns = ["roomName","CheckIn","CheckOut"]
print(df)

#For each stay of GRANT KNERIEN in the hotel, calculate the 
#total amount of money, he paid. Report reservation code, checkin 
#and checkout dates, room name (full) and the total amount of money the stay cost.
#Sort output in chronological order by the day of arrival.
c.execute("""SELECT reservations.Code,reservations.CheckIn,reservations.CheckOut,
          Rooms.roomName,SUM(reservations.Rate) FROM reservations,Rooms
          WHERE (reservations.Room = Rooms.RoomId)
          AND reservations.FirstName LIKE '%GRANT%'
          AND reservations.LastName LIKE '%KNERIEN%'
          ORDER BY reservations.CheckIn""")
df = pd.DataFrame(c.fetchall())
df.columns = ["Code","CheckIn","CheckOut","roomName","Rate"]
print(df)

# For each reservation that starts on December 31, 2010 report 
#the room name, nightly rate and the total amount of money paid.
# Sort output in descending order by the number of nights stayed.

