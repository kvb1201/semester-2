'''
Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
'''
import random

rand100 = list(range(100))
for i in range (100):
    rand100[i] = random.randint(0,1)

    
print(rand100)

maxCount =0
currentCount =0

for nums in rand100:
    if(nums== 0):
        currentCount += 1
    else:
        maxCount = max(maxCount,currentCount)
        currentCount = 0
        
print(maxCount)
    
    