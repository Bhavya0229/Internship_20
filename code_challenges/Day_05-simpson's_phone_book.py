# simpsons_phone_book
#we will use file handling concept
#import re
#^J[a-z]*\s[Neu][a-z]*\s\d{3}\D\d{4}

"""
fh = open("simpsons_phone_book.txt",'r')
fh.readline()
fh.read()
fh.readlines()
fh.close()
"""
# My solution
import re
fh = open("simpsons_phone_book.txt",'r')

for line in fh:
    if (re.search(r'^J[a-z]*\s[Neu][a-z]*\s\d{3}\D\d{4}', line)):
        print (line)

fh.close()

# video solution
import re
fh = open("simpsons_phone_book.txt",'r')

for line in fh:
    if(re.search(r'^J\w*\s*(Neu)', line)):
        print(line)
        
fh.close()
    



