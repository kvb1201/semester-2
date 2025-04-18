#python program to find factorial of a number
number = int(input("Enter the number: "))
i =1
fact =1
while(i <= number):
    fact *= i
    i +=1

print("Factorial of entered number is",fact)