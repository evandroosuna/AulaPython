var = input("Insira um número: ")
numero = int(var)

if numero > 0:
    mensagem = ("Positivo")
elif numero < 0:
    mensagem = ("Negativo")
else:
    mensagem = ("O número é 0")
    
print (mensagem)