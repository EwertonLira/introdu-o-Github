
from control.classLivro import *

def visualizarMenu():
    print('''
        📚 Biblioteca Livre 📚

Sistema de controle de alugueis de livros:
Escolha uma das opções[] abaixo e tecle [Enter↵]

[1] 📝👪 Cadastro de Clientes
[2] 📝🗓️ Alugar livro
[3] 📝📕 Cadastrar livro
[4] 👀👪 Visualizar lista de Clientes
[5] 👀🗓️️ Visualizar lista de alugueis
[6] 👀📕️ Visualizar lista de livro
[0] 🚪 Sair
    ''')

def outrasVisualizacao():
    pass



def imprimirLivro(obj):

    print(f'''
    ID - {obj._id}
    Nome - {obj.getNome()}
    Número de páginas - {obj._paginas}
    Ano de lançamento - {obj._anoLancamento}
    Autor - {obj._autor}
    ''')

imprimirLivro(livroTeste)








def ModifcarArquivoSQL():
    caminho = "Biblioteca\model\createTable.sql"
    with open(caminho, mode="r",newline="") as fileInsertSql:
        arquivoSql = fileInsertSql.read()
        listaInsertSql = arquivoSql.split("-- splitKeyComment insert")
        
        del listaInsertSql[0]
        del listaInsertSql[-1]

        for indice, file in enumerate(listaInsertSql):
            print(indice, file)
        

    with open(caminho, mode='r') as arquivo:
        # ler o conteúdo do arquivo
        conteudo = arquivo.read()

        # substituir a palavra "antiga" pela palavra "nova"
        novo_conteudo = conteudo.replace("Paulo de tarso", "'Paulo de tarso'")

    with open(caminho, mode='w') as arquivo:
        # escrever o conteúdo atualizado no arquivo
        arquivo.write(novo_conteudo)





    with open(caminho, mode="r",newline="") as fileInsertSql:
        arquivoSql = fileInsertSql.read()
        listaInsertSql = arquivoSql.split("-- splitKeyComment insert")
        
        del listaInsertSql[0]
        del listaInsertSql[-1]

        for indice, file in enumerate(listaInsertSql):
            print(indice, file)