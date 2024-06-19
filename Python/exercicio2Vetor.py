numeros =[42, 18, 35, 9, 23, 56, 78, 2, 16, 7, 49, 15, 32, 12, 6, 41, 25, 30, 3, 14,
         50, 11, 38, 21, 67, 72, 31, 8, 29, 45, 17, 5, 19, 27, 61, 10, 54, 13, 22,
         47, 63, 74, 1, 4, 37, 64, 57, 53, 20, 36, 48, 70, 24, 51, 75, 28, 69, 43,
         60, 39, 71, 58, 55, 68, 26, 34, 59, 40, 66, 46, 76, 33, 62, 44, 65, 73, 52,
         77, 79, 80]
menorElemento=numeros[0]
posicao = 0

for i in range (1, len (numeros)):
    if numeros[i] < menorElemento:
        menor_elemento=numeros[i]
        posicao= i
print (f"O menor elemento do vetor é {menorElemento} e está na posição {posicao}")
