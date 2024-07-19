import mysql.connector
from mysql.connector import Error

# define parametros de conexao
db_config = {
    'usuario': 'root',
    'senha': '',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'escola'    
}

# classe TipoAtividade
class TipoAtividade:
    codigo = []
    descricao = ''
    
    def __init__(self, descricao):
        self.descricao = descricao

# obter lista atividades novas        
def obter_atividade_a_excluir():
    codigo_atividade = 0
    print()
    codigo = int(input("Informe a código do Tipo de Atividade a excluir: "))
    return codigo

# imprimir lista atividades informadas
def imprimir_lista_atividade(lista_atividades):
    print()
    print('Lista de Atividades informadas')
    print('------------------------------')

    if len(lista_atividades) > 0:
        for atividade in lista_atividades:
            print("Código {0} = {1}".format(atividade.codigo, atividade.descricao))
    else:
        print("Não foram encontrados tipos de atividade a cadastrar")

    print()

            
# programa principal
codigo_atividade = obter_atividade_a_excluir()

# processo banco de dados
## conectar o banco
conexao = None
try:
    conexao = mysql.connector.connect(host = db_config['host'], port = db_config['port'],
                                      user = db_config['usuario'], passwd = db_config['senha'],
                                      db = db_config['database'])
    
    ## excluir a atividade
    cursor = conexao.cursor()

    delete_sql = """DELETE FROM tiposatividade WHERE codigo = %s)"""
    
    registro = (codigo_atividade, ) 
        
    cursor.execute(delete_sql, registro)
        
    conexao.commit()
   
    cursor.close()
    
except Error as e:
    print("Ocorreu um erro: {0}".format(e.msg))

finally:
    if conexao != None:
        if conexao.is_connected:
            conexao.close()