# Decode the message:
# A message containing the letters from A-Z can be encoded into the numbers using the mapping
# A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
# and do the reverse mapping. You are required to display all the possible decoded messages.
# For example: "11106" can be decoded into:
# a. "AAJF" with the grouping (1 1 10 6)
# b. "KJF" with the grouping (11 10 6)

def decode_ways(s, result=""):
    if not s:
        print(result)
        return
    if s[0] != "0":
        decode_ways(s[1:], result + chr(int(s[0]) + 64))
    if len(s) > 1 and "10" <= s[:2] <= "26":
        decode_ways(s[2:], result + chr(int(s[:2]) + 64))

decode_ways(input("Enter the code: "))



        
    
    
    

