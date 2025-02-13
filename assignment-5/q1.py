# Maximizing XOR
L = int(input("Enter the left limit: "))
R = int(input("Enter the right limit: "))
ans = 0
if(R>=L and L >=1 and R<=1000):
    for start in range(L,R+1):
        for end in range(start+1,R+1):
            if(start == end):
                continue
            elif(start%2 == end%2):
                continue
            else:
                ans = max(ans,start^end)
                
print(ans)
