
list1=[1,2,3,4,5,6,7]

type(list1)

str1="Forsk Coding School"

print(str1)

#indexing and slicing
str1[0:10]

str1[10:]

str1[:10]

#string operations

dir(str)

help(str.upper)

str1.upper()
#strings are read only
#strings are immutable

str1.lower()

#math library

import math
dir(math)
help(math.sqrt)
x=input("Enter the number: ")

x= int(x)
math.sqrt(x)

#version 1
while (True):
    x=input("Enter the number: ")
    if (not x):
        print('Invalid input..leaving app')
        break
    x= int(x)
    print(math.sqrt(x))

#version 2    
while (True):
    x=input("Enter the number: ")
    if (not x):
        print('Invalid input..try next')
        break
    
    if(x.isdigit()):
        x= int(x)
        print("the square root is", math.sqrt(x))
    else:
        print("the length is", len(x))
        
#version 3

datastore = []
while (True):
    x=input("Enter the number: ")
    if (not x):
        print('Invalid input..try next')
        break
    
    if(x.isdigit()):
        x= int(x)
        datastore.append(math.sqrt(x))
    else:
        datastore.append(len(x))
print(datastore)
    
    


