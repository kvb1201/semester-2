# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a
# product name and print the corresponding price or a message if the product is not in the
# dictionary.
print("Entering list items")
print("Enter 0 to exit and 1 to continue:")
UserInput = int(input())
if(UserInput != 0 and UserInput!= 1):
    print("Invalid Input")
else: 
    dictionary = dict()
    while(UserInput):
        item = input("Enter item name: ")
        price = input("Enter price: ")
        temp = {item: price}
        dictionary.update(temp)
        print("Enter 0 to exit and 1 to continue:")
        UserInput = int(input())
    if(len(dictionary) != 0):
        print("Exploring the list\n")
        newInput = int(input("Enter 0 to exit and 1 to continue:"))
        if(UserInput != 0 and UserInput!= 1):
            print("Invalid Input")
        else: 
            while(newInput):
                item = input("Enter item to be searched: ")
                if(dictionary.get(item) != None):
                    print(dictionary.get(item))
                else:
                    print("Item not found")
                newInput = int(input("Enter 0 to exit and 1 to continue:"))
            
    

    
    
    

    
    
    

