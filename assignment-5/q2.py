#Halloween Party
T = int(input("Enter the number of testcases: "))
K = []
for i in range(T):
    K.append(int(input("Enter the value of K: ")))

for num in K:
    if(num >=1 and num <= 10):
        if(num != 1 and num !=2):
            if(num%2==0):
                print((num/2)*(num/2))
            else:
                print((int(num-1)/2 * (num+1)/2))
                
    

