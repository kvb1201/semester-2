# rindex and rfind function

def rIndex(str,searchString):
    found = 0
    start = len(str)
    span = len(searchString)
    while(start-span >=0):
        subStr = str[start-span:start]
        if(subStr == searchString):
            print("String found")
            found =1
            break
        else:
            start -=1
    if(found == 1):
        return start-span
    else:
        print("String not found")
        return -1
    

str = input("Enter the string: ")
searchString = input("Enter the string to be searched: ")

ind = rIndex(str,searchString)
print(ind)
    






