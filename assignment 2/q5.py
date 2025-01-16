'''You are a student in a class of 10. Your class teacher assigns you a task of entering the
names of all the students in the class. You finally want to display the names given the
condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
names and display them. [Hint: Slicing works when you are selecting maximum characters]
'''

nameList = []
for i in range(10):
    name = input("Enter your name: ")
    if(len(name) > 15):
        newname= name[:15]
        reversedName = newname[::-1]
        nameList.append(reversedName)
    else:
        reversedName = name[::-1]
        nameList.append(reversedName)

print(nameList)

