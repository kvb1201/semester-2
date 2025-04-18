# Write a Pandas program to convert all the string values to upper, lower cases in a given
# pandas series. Also find the length of the string values.
# s = pd.Series ([‘X’, ‘Y’, ‘T’, ‘Aaba’, ‘Baca’, ‘CABA’, None, ‘bird’, ‘horse’, ‘dog’])

import pandas as pd

def converterU(s):
    new_series =pd.Series([(str(ele).upper(),len(str(ele))) for ele in s ])
    return new_series

def converterL(s):
    new_series = pd.Series([ (str(ele).lower(),len(str(ele))) for ele in s])
    return new_series

s = pd.Series(['X','Y', 'T', 'Aaba', 'Baca', 'CABA',None, 'Bird', 'horse','dog' ])
print('Lower cased ')
print(converterL(s))
print('\nUpper cased')
print(converterU(s))
