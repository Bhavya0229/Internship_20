# Employee class

class Employee:
    
    num_of_emp=0
    
    

    def __init__(self,first_name,last_name,salary):  #dunder methods
        self.first = first_name
        self.last = last_name
        self.pay = salary
        self.email = first_name.lower()+"."+last_name.lower()+"@infosys.com"
        #print("Inside Employee constructor")
        Employee.num_of_emp += 1
        
    def fullname(self):
        return self.first + " " + self.last
        
emp_1 = Employee("Bhavya","Garg",50000)  #constructor
#print(emp_1)

emp_2 = Employee("Ridhima","Gupta",40000)
#print(emp_2)
print(Employee.num_of_emp)
print(emp_1.fullname())
print(emp_2.fullname())
print(Employee.fullname(emp_1))

#Manager Developer

class Manager(Employee):
    pass

class Developer(Employee):
    pass

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))

#multiple inheritance

class A:
    pass
class B:
    pass
class C(A,B):
    pass





