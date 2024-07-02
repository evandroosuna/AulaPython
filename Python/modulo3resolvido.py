# classe Loja
class Loja:
    def __init__(self, nome, valorArrecadado = None):
        self.nome = nome
        if valorArrecadado == None:
            self.valorArrecadado = 0.0
        else:
            self.valorArrecadado = valorArrecadado    

# classe Compra
class Compra:
    nome = ""
    valor = 0.0
    valorPagar = 0.0
    desconto = 0.0
    
    def calcularDesconto(self):
        if self.valor >= 250.0:
            self.desconto = 20 / 100
        else:
            self.desconto = 15 / 100
        
        self.valorPagar = self.valor * (1 + self.desconto)
       
# ler arquivo com compras            
def obterCompras():
    listaCompras = []
    arquivo = None
    
    try:
        arquivo = open('python\\meuArquivo.txt', 'r')
        for linha in arquivo:
            dadosCliente = linha.split(',')
            compra = Compra()
            compra.nome = dadosCliente[0]
            compra.valor = float(dadosCliente[1])
            compra.desconto = 0.0
            compra.valorPagar = 0.0
            
            listaCompras.append(compra)

    except FileNotFoundError as f:
        print("\nArquivo não encontrado: " + str(f) + "\n")

    except Exception as e:
        print("\nErro ao acessar o arquivo: " + str(e) + "\n")

    else:
        arquivo.close()
        
    return listaCompras

# processar os Descontos de cada compra
def processarDesconto(listaCompras): 
    for compra in listaCompras:
        compra.calcularDesconto()
        
# processar o valor Arrecadado da Loja a partir de cada compra        
def processarValorArrecadado(listaCompras):
    valorArrecadado = 0.0
    for compra in listaCompras:
        valorArrecadado += compra.valorPagar
    
    return valorArrecadado

# imprimir o resultado
def imprimirResultado(loja, listaCompras):
    print()
    print("A loja {0} arrecadou R$ {1:.2f} devido às seguintes compras:".format(loja.nome, loja.valorArrecadado))
    print("----------------------------------------------------------------------")
    print("Nome \t\t Valor \t\t Desconto \t Valor Pagar")
    print("----------------------------------------------------------------------")
    for compra in listaCompras:
        print("{0} \t {1:.2f} \t {2:.2f} \t\t {3:.2f}".format(compra.nome, compra.valor, compra.desconto, compra.valorPagar))
    print()
    

# programa principal
loja = Loja("Baratão")

compras = obterCompras()
processarDesconto(compras)
loja.valorArrecadado = processarValorArrecadado(compras)
imprimirResultado(loja, compras)