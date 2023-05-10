from control.classConexao import *
from model.classLivro import *
from view.menu import *

# ----- início instâncias -----------
livro = Livros()

conetBiblio = Conexao("Biblioteca","localhost","5432","postgres","postgres")

#--------------fim instâcias -----------

#------------ inicío ------------
resultado = conetBiblio.consultarBanco(livro.consultarLivro())
if len(resultado) >= 0:
    print("banco de Dados pronto para uso")
else:
    conetBiblio.manipularBanco(livro.criarTabela())
    conetBiblio.manipularBanco(cliente.criarTabela())
    conetBiblio.manipularBanco(aluguel.criarTabela())
    conetBiblio.manipularBanco(autor.criarTabela())

while True:
    
    op = visualizarMenu()
    
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            livro.setInputDados()
            resultado = conetBiblio.manipularBanco(livro.cadastrarLivro())
            if resultado:
                mensagemDeconfirmacao()
            else:
                mensagemDeNegacao()
        case "4":
            pass
        case "5":
            pass
        case "6":
            resultado = conetBiblio.consultarBanco(livro.consultarLivro)
            if resultado:
                print("ID | Nome do livro:)
                for livro in resultado:
                    print(f'''
                    ''')

                
            else:
                mensagemDeNegacao()
        case "0":
            print("saindo do programa")



