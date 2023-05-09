
from control.classConexao import *
from control.classSetSQL import *
from model.classAluguel import *
from model.classCliente import *
from model.classLivro import *
from view.menu import *

def modificaSQL(coluna,split,variávelEscolhida, idEscolhido):

    with open("model\comandos.sql", mode='r') as arquivo:
        # ler o conteúdo do arquivo
        conteudo = arquivo.read()

        # substituir a palavra "antiga" pela palavra "nova"
        novo_conteudo = conteudo.replace(variávelEscolhida, idEscolhido)

    with open("model\comandos.sql", mode='w') as arquivo:
        # escrever o conteúdo atualizado no arquivo
        arquivo.write(novo_conteudo)

    with open("model\comandos.sql", mode="r",newline="") as fileInsertSql:
        arquivoSql = fileInsertSql.read()
        listaSql = arquivoSql.split("-- splitKeyComment " + split)
        
        del listaSql[0]
        del listaSql[-1]

        for comando in listaSql:
            if coluna in comando:
                sql = comando
    
    return sql



conexaoBiblioteca = Conexao("Biblioteca", "localhost", "5432", "postgres", "postgres")
livro = Livros()
livro.setDadosLivro()
# comandosSqlLivro = SetSQL(livro)

opEscolhida = visualizarMenu()

match opEscolhida:
    case "6":
        # comandosSqlLivro.verlivros()
        sql =modificaSQL("livros","IDselect","{livroIDSelect}","777")
        print(sql)
        conexaoBiblioteca.manipularBanco()




# # setAluguel = setSQL(objAluguel)
# # setCliente = setSQL(objCliente)

# setLivro.verificarObj()

# ArquivoSQL = SetSQL(objlivro,"insert")
