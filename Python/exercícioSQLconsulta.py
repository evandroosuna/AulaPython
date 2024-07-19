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
    codigo = 0
    descricao = ''
    
    def __init__(self, descricao = None):
        self.descricao = descricao

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
lista_atividades = []

# processo banco de dados
## conectar o banco
conexao = None
try:
    conexao = mysql.connector.connect(host = db_config['host'], port = db_config['port'],
                                      user = db_config['usuario'], passwd = db_config['senha'],
                                    db = db_config['database'])
    
    #print(conexao.is_connected())

    ## incluir a atividade
    cursor = conexao.cursor()
    
    select_sql = """SELECT * FROM tiposatividade"""
        
        
    cursor.execute(select_sql)

    resultado = cursor.fetchall ()
    
    #monta a lista com objetos a partir do resultado da consulta
    for registro in resultado:

        #criando o objeto tipo atividade
        obj_tipo_atividade = TipoAtividade ()
        #populando as propriedaes do objeto criado 
        obj_tipo_atividade.codigo = registro [0]
        obj_tipo_atividade.descricao = registro [1]
        lista_atividades.append(obj_tipo_atividade)

    

    cursor.close() 
    
except Error as e:
    print("Ocorreu um erro: {0}".format(e.msg))

 

finally:
    if conexao.is_connected:
        conexao.close()
imprimir_lista_atividade(lista_atividades)