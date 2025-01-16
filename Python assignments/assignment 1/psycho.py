#counting minimum number of swaps to sort a list
swapCounter =0
n =int ( input("Enter the size of list:"))
original_list = []
for i in range(n):
    original_list.append((int(input("Enter the number: ")),i))

print (list)
sorted_list = sorted(original_list, key=lambda x : x[0])

print(sorted_list)

i =0
while i <n:
    if(original_list[i][1] == sorted_list[i][1]):
        i+=1
    else:
        original_list[i],original_list[sorted_list[i][1]] = original_list[sorted_list[i][1]],original_list[i]
        swapCounter+=1


print(swapCounter)



