'''1. Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of the integers 1 through 50.
(c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.
'''

#a 
numList =[]
for i in range(50):
    numList.append(i)
    
# print (numList)
#b
squareList = []
for i in range(1,51):
    squareList.append(i*i)

# print(squareList)
#c
alphaList = []

for i in range(1,27):
    
    for j in range (1,i+1):
        str = chr(96+i) * j
    
        
    alphaList.append(str)
    
print(alphaList)
    
    
    

        
    
