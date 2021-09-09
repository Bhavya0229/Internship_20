# Number game


#print ("Guess the number from 1 to 10: ")
#import math

# My solution
secret_number = 2
print ("Guess the number from 1 to 10: ")
x = input("Enter the number: " )
x = int(x)
if (x == secret_number):
    print("Player wins and computer lose")
else:
    print("Player lose and computer wins")

#video solution
import random
secret_number = random.randint(1, 10)
print ("Guess the number from 1 to 10: ")
x = input("Enter the number: " )
x = int(x)
if (x == secret_number):
    print("Player wins and computer lose")
else:
    print("Player lose and computer wins")




