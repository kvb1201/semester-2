#N is the Number boxes and S is the number of swaps and the X is
t = int(input())
for j in range(t):
    #in each swap we have to take input from the user
    N,X,S = map(int,input("").split())

    for i in range(S):
        a,b = map(int,input("").split())
        


        if(a == X) :
            
            X = b

        elif(b == X):
            
            X = a
    
print(X)