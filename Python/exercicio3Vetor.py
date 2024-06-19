import random

numero=[]

for contador in range (15):
    numero = random.randint(-20,20)
    numero.append (numero)

    if num % 2 ==0:
        print (f"O {num} é par")
    else:
        print (f"O {num} é ímpar")

