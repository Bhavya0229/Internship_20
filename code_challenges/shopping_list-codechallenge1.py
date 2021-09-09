#Shopping list
"""
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT 
    the program
    And once i quit, I want the app to show me 
    everything thats
    on my list.

Hint:
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use 
    the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""

# My first try

Sh_list = []
print ("What should we pick up at the store?")
print ("Press 'DONE' to stop adding items.")

while (True):
    new_item = input("Enter any item: ")
    if (new_item == 'DONE'):
        break
    Sh_list.append(new_item)
    
print("Here is your list items: ")

for item in Sh_list:
    print(item)
   


    
        
        









        
    
