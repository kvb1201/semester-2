# You are given a number N, you need to print the number of positions where digits exactly
# divides N.

testCases = int(input("enter number of testcases: "))
if(testCases >=1 and testCases <=15):
    numbers = list(range(testCases))
    for i in range(testCases):
        num = int(input("Enter the number:"))
        numbers[i] = num

    for i in range(testCases):
        counter =0
        temp = str(numbers[i])
        for digit in temp:
            if(int(digit) !=0):
                if(int(temp)%int(digit) == 0):
                    counter +=1

        print(counter)
else:
    print("invalid input")   
