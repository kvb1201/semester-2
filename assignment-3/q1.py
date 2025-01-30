# The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
# Add up the digits of that to get another new number. Keep doing this until you get a number
# that has only one digit. That number is the digital root. For example, if n = 45893, we add up
# the digits to get 4+5+8+9+3=29. We then add up the digits of 29 to get 2+9 = 11. We then add
# up the digits of 11 to get 1+1 = 2. Since 2 has only one digit, 2 is our digital root. Write a
# function that returns the digital root of an integer n. [Note: there is a shortcut, where the digital
# root is equal to n mod 9, but do not use that here.

num = input("Enter the number: ")
digits = len(num)
sum =0
while(digits != 1):
    sum =0
    for i in num:
        sum+= int(i)
    digits = len(str(sum))
    num = str(sum)
    
print(sum)
    
    