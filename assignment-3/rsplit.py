def rSplit(str,sep):
    splitList = []
    start =0
    end =0
    found =0
    for chars in str:
        if(chars != sep):
            end +=1
            
        else:
            found =1
            splitList.append(str[start:end])
            end +=1
            start = end
    if(found == 0):
        splitList.append(str)
    return splitList


print(rSplit("Kavya","m"))
print("kavya".rsplit("m"))






        


        
