###############################################################################
############# pré-requisitos para rodar o arquivo mainDB.py  ##################
###############################################################################
# 
# instale as seguintes bibliotecas no padrão python:
# psycopg2
# Pillow
# requests

from PIL import Image
from io import BytesIO
import requests

from classConexao import *
from sqlScript import *
import env

# criada conexão com o banco de dados:
conexao = Conexao(env.dbname, env.host, env.port, env.user, env.password)

# conexao.manipularBanco('''CREATE TABLE "Teste" (
#     "teste_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     "teste_cep" varchar(255) NOT NULL
#     );
# ''')
    
def criarTabelas():
    resultado = conexao.manipularBanco(sqltabelas)
    if resultado:
        print("tabelas criadas com sucesso")
    else:
        print("ocorreu um erro na criação de tabelas")

def BDinsertCliente(BDinsertEndereco):
    # função para inserir um cliente no banco de dados
    
    # id já está configurado no banco de dados
    nome = input("insert name: ") # o imput pode ser substituido por uma variável vinda de outro script
    telefone = input("insert phone: ")
    email = input("insert email: ")
    
    # chama a outra função
    BDinsertEndereco()
    

    idEndereco = conexao.consultarBanco('''SELECT "endereco_id" FROM "endereco"''')
    endereco = idEndereco[0][-1]
    # status vai com o valor padrão "ativo" para o banco de dados


    resultado = conexao.manipularBanco(f"""
    INSERT INTO "cliente"
    VALUES (DEFAULT,'{nome}','{telefone}','{email}','{endereco}',DEFAULT)
    """)
    if resultado:
        pass
    else:
        print("ocorreu um erro na tabela cliente")
    
    return BDinsertCliente

def BDinsertEnderco():
    # cadastrar um endereço no banco de dados, só cadastra um endereço juntamente com um cliente
    
    # id já está configurado no banco de dados
    cep = input("insert CEP: ") # a função input pode ser trocada por uma variável
    uf = input("insert state federation")
    cidade = input("insert city")
    bairro = input("insert neighborhood")
    rua = input("insert street: ")
    complemento = input("insert complement: ")
    # status vai com o valor padrão "ativo" para o banco de dados

    resultado = conexao.manipularBanco(f"""
    INSERT INTO "endereco"
    VALUES (DEFAULT ,'{cep}','{uf}','{cidade}','{bairro}','{rua}','{complemento}')                                 
    """)
    if resultado:
        pass
    else:
        print("ocorreu um erro na tabela endereco")

def BDinsertOrcamento():
    # função para inserir um orçamento no banco de dados
    
    # id já está configurado no banco de dados
    idCliente = conexao.consultarBanco('''SELECT "cliente_id" FROM "cliente"''')
    cliente = idCliente[0][-1]

    mediaEnergia = input("insert average energy: ")
    mediaPagamento = input("insert average payment: ") # o imput pode ser substituido por uma variável vinda de outro script
    TipoResidencia = input("insert type residence: ")
    valorInstalar = input("insert installantion values: ")
    # data e adicionada automáticamente como padrão 
    # status vai com o valor padrão "ativo" para o banco de dados

    resultado = conexao.manipularBanco(f"""
    INSERT INTO "orcamento"
    VALUES (DEFAULT,'{cliente}','{mediaEnergia}','{mediaPagamento}','{TipoResidencia}','{valorInstalar}', DEFAULT , DEFAULT)
    """)
    if resultado:
        pass
    else:
        print("ocorreu um erro na tabela orçamento")

def BDinsertProduto():
    # cadastrar um produto no banco de dados
    
    # id já está configurado no banco de dados
    nome = input("insert name: ") # a função input pode ser trocada por uma variável
    valor = input("insert values")
    descricao = input("insert description")
    
    #///////////////////////////////////////////////
    # # para adicionar uma imagem no banco de dados:
    # with open(urlImagem, "rb") as arquivo:
    #     imagemBytes = arquivo.read()
    # #///////////////////////////////////////////////
    urlImagem = input("insira o caminho da imagem ou url")
    resposta = requests.get(url=urlImagem)
    dadosDaImagem = resposta.content
    imagemBytes = BytesIO(dadosDaImagem).read()
    
    # status vai com o valor padrão "ativo" para o banco de dados

    resultado = conexao.manipularBanco(f"""
    INSERT INTO "produto"
    VALUES (DEFAULT ,'{nome}','{valor}','{descricao}', {psycopg2.Binary(imagemBytes)} ,DEFAULT)                                 
    """)
    if resultado:
        pass
    else:
        print("ocorreu um erro na tabela endereco")

def recuperarImagem():
    idEscolhido = input("insert id image: ")
    resultado = conexao.consultarBanco(f'SELECT "produto_imagem" FROM "produto" WHERE produto_id = {idEscolhido}')
    resultadoImagem = resultado[0][0]
    
    dados = BytesIO(resultadoImagem)
    imagem = open(dados, "wb")
    imagem = Image.open(resultadoImagem)
    
    # Abrir a imagem no visualizador padrão
    imagem = Image.open("imagem.jpg")
    imagem.show()

    #///////////////////////////////////////////////
    # # Salvar o arquivo binário como imagem
    # with open("imagem.jpg", "wb") as arquivo:
    #     arquivo.write(resultadoImagem)
    #///////////////////////////////////////////////

################## início do código ######################
# criarTabelas()

# BDinsertCliente(BDinsertEnderco)
# print("agora crie um orçamento")
# BDinsertOrcamento()
# print("agora adicione um produto ao banco de dados")
# BDinsertProduto()

input("tecle enter para continuar recuperar imagem")
recuperarImagem()
