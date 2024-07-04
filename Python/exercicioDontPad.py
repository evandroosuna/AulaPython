def CalculoCaracter():
    listaPalavras = []
    arquivo=open('python\\word.txt','r')
    for linhas in arquivo: 
        palavras=linhas.split(' ')
        listaPalavras.append(palavras)
        arquivo.close
        if palavras in listaPalavras (len(palavras))> 20:
            return listaPalavras
    print (f'As palavras com menos de 20 caracteres são: {listaPalavras}')


CalculoCaracter()
    