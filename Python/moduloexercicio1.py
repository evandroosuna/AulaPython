def reajuste (taxa, salario):
    taxaPercentual=taxa/100
    novoSalario = salario + salario * taxaPercentual
    return novoSalario

class Trabalhador:
    nome = ''
    salario = 0
    
    def __init__(self,nomeTrabalhador,salarioTrabalhador):
        self.nome = nomeTrabalhador
        self.salario = salarioTrabalhador
        
#inicio do programa
listaTrabalhadores =[]

#entrada
for i in range(3):
    nome=input('Informe o nome do {0}o. Trabalhador: '.format(i+1))
    salario=float(input('Informe o salário do trabalhador: '.format(i+1)))
    
    trabalhador=Trabalhador(nome,salario)
    listaTrabalhadores.append(trabalhador) 

for trabalhador in listaTrabalhadores:
    print('O trabalhador se chama {0} e seu salário é de R${1:.2f}'.format(trabalhador.nome,trabalhador.salario))
    salarioReajustado= reajuste(8,trabalhador.salario)
    trabalhador.salario = salarioReajustado

for trabalhador in listaTrabalhadores:
    print('O Trabalhador se chama {0} e seu salário reajustado é de R$ {1:.2f}'.format(trabalhador.nome, trabalhador.salario))
       
  
#trabalhador = Trabalhador('Marcos',10000)
#print('O trabalhador se chama {0} e seu salário é R${1:.2f}'.format (trabalhador.nome, trabalhador.salario))
#salarioReajustado= reajuste(10,trabalhador.salario)
#trabalhador.salario = salarioReajustado
