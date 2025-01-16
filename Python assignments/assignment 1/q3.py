#python program to swap two variables without using third variable

var_1 = int(input("Value of variable 1:"))
var_2 = int(input("Value of variable 2:"))

var_1 = var_1 + var_2
var_2 = var_1 - var_2
var_1 = var_1 - var_2

print("Value after swapping of variable 1 and variable 2 is ",var_1,"and", var_2,"respectively", )