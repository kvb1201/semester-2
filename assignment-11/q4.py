# Whenever your friends John and Judy visit you together, y’all have a party. Given a
# DataFrame with 10 rows representing the next 10 days of your schedule and whether John
# and Judy are scheduled to make an appearance, insert a new column
# called days_til_party that indicates how many days until the next party.
# days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn’t
# occur but will occur the next day, etc.

import pandas as pd

# Sample data for 10 days
data = {
    'day': pd.date_range(start='2025-04-05', periods=10, freq='D'),
    'John':    [True, False, True, False, True, False, False, True, False, True],
    'Judy':    [True, True, False, False, True, False, True, True, False, False]
}


party_days = []
for i in range(10):
    if data['John'][i] == True and data['Judy'][i] == True:
        party_days.append(True)
    else:
        party_days.append(False)
    
print(party_days)

     
days_til_party =[x*0 for x in range(10)]
# 

for i in range(10):
    if party_days[i] == True:
        continue
    else:
        j =0
        k=i
        no_party = 1
        
        if party_days[k] == False:
            while (k <10):
                if party_days[k] == True:
                    no_party=0
                k+=1
        
        k=i
        if no_party == 0:
            while(k <10 and party_days[k] == False):
                j+=1
                k+=1
        else:
            j =-1
        days_til_party[i] = j


print(days_til_party)

data.update({"days_til_Party":days_til_party})
df = pd.DataFrame(data)
print(df)    
    
    
    


        
           
        
    