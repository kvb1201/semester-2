'''Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.
'''
length = int(input("Enter the length in feet : "))
userInput = int(input("Enter 1 for conversion to inches \n\
Enter 2 for conversion to yards \n\
Enter 3 for conversion to millimeters\n\
Enter 4 for conversion to centimeters \n\
Enter 5 for conversion to kilometers:\n"))

convertList = [12,0.33,0.000189,300,30,0.0003048]

print(length * convertList[userInput-1])