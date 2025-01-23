# Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.
inputWord = input("Enter the word: ")
newWord = []
for i in range(len(inputWord)):
    if(i%2 ==1):
        word = inputWord[i].capitalize()
        newWord.append(word)
    else:
        newWord.append(inputWord[i])
        
inputWord = "".join(newWord)
print(inputWord)


    
    
        
   
        
