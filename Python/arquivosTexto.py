arquivo= open('meuArquivo.txt', 'wt')
arquivo.write('Ola tudo bem?\n')
arquivo.write('Onde esta?\n')
arquivo.close()

arquivo=open('meuArquivo.txt','r')
print(arquivo.read())
arquivo.close()