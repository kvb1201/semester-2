# Pangrams
inputString = input("Enter the string: ")
lowercase_alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
alphaSet = set(lowercase_alphabet)
inputSet = set(inputString)
if(alphaSet.issubset(inputSet)):
    print("pangram")
else:
    print("not pangram")
