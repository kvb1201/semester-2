def lexGreat(word):
    n = len(word)
    flag = 0

    for i in range(n-1,1,-1):
        if(word[i] > word[i-1]):
            flag =1
            stopIndx =i-1
            letter = word[i-1]
            break
    if flag == 1:
        aux = []
        for i in range(n):
            if(word[i] >letter):
                aux.append((word[i],i))

        aux = sorted(aux ,key= lambda x:x[0])
        word = list(word)
        word[stopIndx],word[aux[0][1]] = word[aux[0][1]],word[stopIndx]
        

        word = sorted(word[:stopIndx-1])+ word[stopIndx-1:]
        return "".join(word)
    else:
        return "no answer"
    
t = int(input("Enter the number of testcases: "))
words = []
for i in range (t):
    words.append(input("Enter the word: "))

for word in words:
    print(lexGreat(word))

















    
    
    


        


    





