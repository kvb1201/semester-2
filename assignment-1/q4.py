'''
Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence
classes should be the original set/list.
'''
univSet = set()
for i in range(1, 10001):
    univSet.add(i)
    
setList = list(range(5))
for i in range(5):
    setList[i] = set()
    
for i in range(1,10001):
    setList[i%5].add(i)
    
print(setList[0])




    

    
        