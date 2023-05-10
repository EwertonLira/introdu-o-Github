
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
    op = input(": ")
    return op

def mensagemDeconfirmacao():
    print("O registro efetuado com sucesso")

def mensagemDeNegacao():
    print("O registro Falhou. verifique os dados inseridos e tente novamente")

def imprimirListaLivros(listaLivros):
    print("ID | nome do livro")
    for livro in listaLivros:
        print(f"{livro[0]} - {livro[1]}")

