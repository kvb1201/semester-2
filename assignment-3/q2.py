# You are given a integer, N. Write a program to determine if N is an element of the Fibonacci
# Sequence.
def fibN(n):
    if(n==1  or n== 0):
        if(n==1):
            return 1
        if(n==0):
            return 0
    else:
        return fibN(n-1)+fibN(n-2)

def isFibo(N):
    i =1
    while(fibN(i) <= N):
        i+=1
        
    if(fibN(i-1) == N):
        print("IsFibo")
    else:
        print("IsNotFibo")
        
        
inputList = []
T = int(input("Enter the number of testcases: "))
for i in range(T):
    num = int(input("Enter the number: "))
    inputList.append(num)
for N in inputList:
    isFibo(N)
    

    
    
    
