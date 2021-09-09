#Create a Book class
"""
Create a Book class which stores the follwing information 
about the book as instance variables:
       authorlast, 
       authorfirst, 
       title, 
       place, 
       publisher, 
       and year
   Also create a instance method:
    "write_bib_entry" 
   which returns a formatted bibliographic reference for the book.
   
2. Create a two instances of Book class in the name of "beauty" and "pynut":
    For getting all the info about authors and other details,
    please make a Google search with below book names:
    book1: The Evidential Power of Beauty
    book2: Python in a Nutshell
    
3. How would you print out the book attribute of the pynut instance?


4. If you type print beauty.write_bib_entry() at the interpreter, what will happen?

5. How would you change the publication year for the beauty book to "2021" and
print it back?
"""
# My solution

class Book:
    
    def __init__(self,first_name,last_name,book_title,place_name,publisher_name,pub_year):
        self.authorfirst = first_name
        self.authorlast = last_name
        self.title = book_title
        self.place = place_name
        self.publisher = publisher_name
        self.year = pub_year
        
    def write_bib_entry(self):
        return self.authorfirst + " " + self.authorlast + " " + self.title + " " + self.place + " " + self.publisher + " " + self.year

beauty = Book("Thomas","Dubay","The Evidential Power of Beauty",
              "San Francisco","Ignatius Press","1 September 1999")

pynut = Book("Alex","Martelli","Python in a Nutshell",
             "Sebastopol,CA","‎ O′Reilly","25 April 2017")

print(Book.write_bib_entry(pynut))
print(pynut.write_bib_entry())

beauty.year = "2021"
print(beauty.write_bib_entry())
