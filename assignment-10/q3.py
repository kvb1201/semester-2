# A magic square is an N×N grid of numbers in which the entries in each row, column and
# main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
# N=4, 5, 6, 7, 8

#Magic square creation method is different for odd n and even n
import numpy as np
#magic square for odd n 
def odd_magicSquare(n):
    magicSquare = np.zeros((n,n),dtype=int)
    i,j = 0,n//2 #starting placing numbers from middle cell of first row
    for num in range(1,n*n+1):
        magicSquare[i][j] = num #placing the number
        #moving one step up and one step right
        
        new_i,new_j = (i-1)%n,(j+1)%n
        if(magicSquare[new_i,new_j]): #moving down if square is already occupied
            i+=1
        else:
            i,j = new_i,new_j

    return magicSquare
#code for magic square with n divisible by 4
def doubly_even_magicSquare(n):
    magicSquare =np.arange(1,n*n+1).reshape(n,n)

    mask = np.zeros((n,n),dtype=bool)
    for i in range(n):
        for j in range(n):
            if (i%4 -j%4 == 0)or (i%4 + j %4 == 3):
                mask[i,j] = True
    
    magicSquare[mask] = n*n + 1 -magicSquare[mask]
    return magicSquare

 #code for magic square with even n not divisible by 4

def singly_even_magicSquare(n):
    half_n = n//2
    subSquare = odd_magicSquare(half_n)

    top_left = subSquare
    top_right = subSquare + 2*(half_n**2)
    bottom_left = subSquare + 3*(half_n**2)
    bottom_right = subSquare + (half_n**2)

    magicSquare = np.block([[top_left,top_right],[bottom_left,bottom_right]])

    cols_to_swap = half_n//2
    for i in range(half_n):
        for j in range(cols_to_swap):
            magicSquare[i, j], magicSquare[i + half_n, j] = magicSquare[i + half_n, j], magicSquare[i, j]

    # Swap last `cols_to_swap - 1` columns in A and C
    for i in range(half_n):
        for j in range(n - cols_to_swap, n):
            magicSquare[i, j], magicSquare[i + half_n, j] = magicSquare[i + half_n, j], magicSquare[i, j]     
    return magicSquare



print("Magic Square of 4")
print(doubly_even_magicSquare(4))
print("\nMagic Square of 5")
print(odd_magicSquare(5))
print('Magic square of 6')
print(singly_even_magicSquare(6))
print('\nMagic square of 7')
print(odd_magicSquare(7))
print('\nMagic Square of 8')
print(doubly_even_magicSquare(8))




