def CalculoDesconto (Desconto, ValorDaCompra):
    Desconto=Desconto/100
    ValorDaCompra = ValorDaCompra-ValorDaCompra*Desconto

class Cliente: 
    Nome =''

class ValorCadaCliente:
    ValorDaCompra=0 
    ValorFinalCliente = 0 

for i in range(1):
    Nome=input('Informe o nome do {0}o. Cliente: '.format(i+1))
    ValorDaCompra=float(input('Informe o Valor da Compra: '.format(i+1)))
    cliente=Cliente(nome)
    listaclientes.append(cliente) 

for 
    
    if ValorDaCompra>250.0:
        
    else:
        ValorFinalCliente=CalculoDesconto(15,ValorDaCompra)

print (f'O cliente {Nome} ira pagar ao final o valor de {ValorFinalCliente}')
    