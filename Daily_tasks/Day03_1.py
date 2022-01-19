#regular expressions

import re

s = 'aaa@gmail.com bbb@yahoo.com ccc@outlook.com'

re.sub('[a-z]*@','ABC@',s)

str1 = '123abc123xyz456_0'
re.findall('^\d\d\d', str1)

str1 = 'fool123bar'
re.search('\d\d\d', str1)

str2 = 'Forsk forsk coding school'
re.match('forsk',str2)
re.search('forsk', str2)
re.match('Forsk', str2)

str1 = 'covid bhavya@gmail.com music priyanshi@outlook.com psych navi@yahoo.in 1234'
epattern = re.compile(r'\w+@\w+\.\w+')
epattern.findall(str1)

