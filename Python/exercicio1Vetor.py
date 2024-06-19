import random

numeros = []
positivos = []

random.seed(80)
for contador in range (80):
    numero = random.randint(-80, 80)
    numeros.append(numero)
    print (numeros)
    
for numero in numeros:
    if numero > 0 and positivos.count(numero)==0:
        positivos.append(numero)
        
print (positivos)
