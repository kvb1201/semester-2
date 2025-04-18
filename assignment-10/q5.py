# Write a program to make the length of each element 15 of a given Numpy array and the
# string centred, left-justified, right-justified with paddings of _ (underscore).

import numpy as np
def converterL(arr):
    new_array = np.array([ele[:15] if len(ele) >15 else ele.ljust(15,'-') for ele in arr])
    return new_array

def converterR(arr):
    new_array = np.array([ele[:15] if len(ele) >15 else ele.rjust(15,'-') for ele in arr])
    return new_array

def converterC(arr):
    new_array = np.array( [ ele[:15] if len(ele) > 15 else ele.center(15, '-') for ele in arr])
    return new_array

arr = np.array(['Hi','I', 'am', 'Artificial Intelligence'])
print(converterL(arr))
print(converterC(arr))
print(converterR(arr))

