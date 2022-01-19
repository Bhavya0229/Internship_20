list1 = [1,2,3,4,5,6,7]

type (list1)

list1[0]

list1[-1]

#Append method 
list1.append(100)

#insert method
list1.insert(1, 22)

#Remove method
list1.remove(5)

list1 = [10,5,2,5,6,5,20]

#count method
list1.count(5)

list1.remove(5)
list1.remove(5)
list1.remove(5)


#using a while loop
list1 = [10,5,2,5,6,5,20]
while(5 in list1):
    list1.remove(5)
    
list1 = ['Amar','Akbar','Anthony']

list1[0]
list1[1]
list1[2]

#using for-each loop
list1 = ['Amar','Akbar','Anthony']
for name in list1:
    print(name)
    
for x in list1:
    print(x)

#calculating the square of each element
list1 = [1,2,3,4,5]
list2 = []
for item in list1:
    list2.append(item*item)

#list comprehension
[item*item for item in list1]

#calculating the length of each element
list1 = ['Amar','Akbar','Anthony']
list2 = []
for item in list1:
    list2.append(len(item))

#list comprehension
[len(item) for item in list1]

"""
name -> Bhavya 
class -> 4
Science -> 89
Psychology -> 90

"""
#dictionary
student = {
    'name' : 'Bhavya',
    'class': 4,
    'Science': 89,
    'Psychology': 90
    }

student['Science']

student['name'] = 'Bhavya Garg'

student = {
    'name' : 'Bhavya',
    'class': 4,
    'Science': 89,
    'Psychology': 90
    }

student['name']= 'Bhavya Garg'

student['city'] = 'Ludhiana'

#version 4
datastore = {}
import math
while (True):
    x=input("Enter the number: ")
    if (not x):
        print('Invalid input..try next')
        break
    
    if(x.isdigit()):
        x= int(x)
        datastore[x] = math.sqrt(x)
    else:
        datastore[x] = len(x)
print(datastore)