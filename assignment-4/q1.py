# The love letter mystery
T = int(input("Enter the number of testcases: "))
if(T>10 or T <1):
    print("Invalid Input")
else:
    inputStrings = []
    for i in range(T):
        inputStrings.append(input("Enter the string: "))

    for string in inputStrings:
        l = len(string)
        opCount =0
        for i in range(l//2):
            if(ord(string[i]) == ord(string[l-i-1])):
                continue
            elif(ord(string[i]) > ord(string[l-i-1])):
                opCount += ord(string[i])-ord(string[l-i-1])
            else:
                opCount += ord(string[l-i-1]) - ord(string[i])
        print(opCount)
