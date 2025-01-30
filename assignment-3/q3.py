# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the
# monsoon, when it doubles in height. The second growth cycle occurs during the summer, when its height
# increases by 1 meter.
# Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find
# the height of the tree after N growth cycles?

def heightAfterN(N):
    height =1
    for i in range(1,N+1):
        if(i%2==0):
            height +=1
        else:
            height*=2
    return height


T = int(input("Enter the number of testcases: "))
inputList = []
for i in range(T):
    inputList.append(int(input("Enter the value of N: ")))
for N in inputList:
    print(heightAfterN(N))    
