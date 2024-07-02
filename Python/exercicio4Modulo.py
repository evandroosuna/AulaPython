class Aluno:
    nome = ''
    notaMatematica= 0
    notaPortugues= 0
    media= 0 
    situacao=''

    def calcularMedia(self):
        self.media= (self.notaMatematica + self.notaPortugues) / 2
        if self.media > 6:
            self.situacao='Aprovado'
        else:
            self.situacao='Reprovado'

#obter alunos

def obterListaAlunos():
    listaAlunos = []
    arquivo=open('python\\AlunosEscola.csv')
    for linha in arquivo:
        dadosAluno=linha.split(',')
        #Construindo e preenchendo o objeto para cada linha
        aluno = Aluno()
        aluno.nome = dadosAluno[0]
        aluno.notaMatematica=float(dadosAluno[1])
        aluno.notaPortugues=float(dadosAluno[2])
        aluno.calcularMedia()
        listaAlunos.append(aluno)
    arquivo.close
    return listaAlunos

def imprimir(alunos):
    for aluno in alunos:
        print(aluno.nome + '\t' + str(aluno.notaMatematica) + '\t' + str(aluno.notaPortugues) + '\t' + str(aluno.media) + '\t' + aluno.situacao)
    

# programa principal
alunos=obterListaAlunos()
imprimir(alunos)
      
