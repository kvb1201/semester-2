# 1. Write a Pandas program to create
# a) Date time object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# t) Time from a date time.
# g) Current local time.

import pandas as pd

date1= pd.Timestamp("2012-01-15")
print(date1)
date1_with_time = pd.Timestamp('15-01-2012 21:20:00')
print(date1_with_time)
local_dt = pd.Timestamp.now()
print('Local date and time:',local_dt)
date_without_time = local_dt.date()
print('Date without time:',date_without_time)
current_date = pd.Timestamp.today().date()
print("Today's data:",current_date)
time = date1_with_time.time()
print(time)
current_time = local_dt.time()
print(current_time)