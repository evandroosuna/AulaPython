Portugues, Matematica, ConhecimentoGerais = 0,0,0
qTdAlunos=3
media=0
PortMedia=0
MatMedia=0
ConhecimentoMedia=0

for i in range(qTdAlunos):
    




###
 qTdAlunos , idade, altura = 5,0,0
somaIdade, qtdIdade = 0,0
somaAltura,qtdAltura= 0,0
idadeMedia = 0 
alturaMedia = 0

for i in range(qTdAlunos):
    idade= int(input("Informe a idade do {0:d}o ".format(i+1)))
    altura = float(input("Informe a altura do {0:d}o ".format(i+1)))
    
    #verificacao da idade
    if altura <1.7:
        somaIdade=somaIdade + idade
        qtdIdade=qtdIdade + 1
        
    
    #verificacao da altura
    if idade > 20:
        somaAltura=somaAltura + altura
        qtdAltura=qtdAltura + 1
    
#calcular as medias de idade e altura
    
idadeMedia=somaIdade / qtdIdade
alturaMedia=somaAltura / qtdAltura
    
#apresentar resultado 
print("A idade média dos alunos é {0:.2f} ano e altura média é {1:.2f}m".format(idadeMedia,alturaMedia))
    