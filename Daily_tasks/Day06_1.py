

list1 = [1,2,3,4,5]

# To find the square of each element 

import maths
list2 = []
for item in list1:
    list2.append(item*item)
    
print(list2)

# Shortcut method
# List comprehension
print([item*item for item in list1])
print([item**3 for item in list1])

#Length of each word in a list

list1 = ['Amar','Akbar','Anthony']
list2 = []
for item in list1:
    list2.append(len(item))
print(list2)
    
print([len(item) for item in list1])

# use of map function

list1 = [10,20,30,40]

def squarevalue(x):
    return(x*x)

print(list(map(squarevalue, list1)))

# to find whether the number is even or not

list1 = [1,2,3,4,5]
def iseven(x):
    if(x % 2 == 0):
        return True
    else:
        return False
    
print(list(map(iseven, list1)))

# filter function is used to filter out the true values
print(list(filter(iseven, list1))) 
 
list1 = [1,2,3,4,5]
def iseven(x):
    return(x % 2 == 0)
print(list(map(iseven, list1)))
print(list(map(lambda x:x % 2 == 0,list1)))

# reduce function

import functools

list1 = [1,2,3,4,5]
def fadd(x,y):
    return(x+y)

print(functools.reduce(fadd, list1))


list1 = [1,2,3,4,5]

def fmul(x,y):
    return(x*y)

print(functools.reduce(fmul, list1))

print(functools.reduce(lambda x,y:x+y, list1))

#dictionary
dict1 = {
    'name':'Bhavya',
    'chem': {'mt1':87,'mt2':92},
    'phy':95,
    'maths':87
    }

# tuples
#unpacking
 
x,y = divmod(32, 5)

t1 = (1,2,3,4,5)
# tuples are read only
# immutable

# concept of class
class Employee:
    pass
emp_1 = Employee()
print(id(emp_1))  #2168222674224
print(emp_1)      #0x000001F8D4246D30





