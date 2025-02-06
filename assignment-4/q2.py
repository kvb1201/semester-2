# Sherlock and Squares
T = int(input("Enter the number of testcases: "))
if(T>100 or T <1):
    print("Invalid Input")
else:
    inputNum = []
    for i in range(T):
        num1 = int(input("Enter the lower limit:"))
        num2 = int(input("Enter the upper limit:"))
        if(num2 >num1):
            inputNum.append([num1,num2])
        else:
            print("Invalid Input")
            i -=1
    
    for nums in inputNum:
        squareCount = ((nums[1]**0.5)//1) - ((nums[0]**0.5)//1)
        print(int(squareCount))



        


