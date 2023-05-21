# sistema de gerenciamento de Biblioteca
from control.classConexao import *
from control.criarTabelas import *
from model.classAluguel import *
from model.classCliente import *
from model.classLivro import *
from view.ClassMsg import *
#_______________________ instanciar classes _____________________

biblioDB = Conexao("Biblioteca","localhost","5432","postgres","postgres")
aluguel = Aluguel()
cliente = Clientes()
livro = Livros()
msg = Msg()
CriarTodasTabelas(biblioDB)
#_______________________ início do while _____________________

op = "rodarWhile"
while op != "0":
    op = msg.visualizarMenu()

    match op:
        case "1": 
            sqlInsertCliente = cliente.cadastrarCliente()
            resultadoInsercao = biblioDB.manipularBanco(sqlInsertCliente)
            msg.mensagemDeConfirmacao(resultadoInsercao)

        case "2":
            vazio = []
            _ = msg.mensagemAlugarLivro("fraseInicial", vazio)
            # visualizar lista de clientes e escolher uma opção
            sqlSelectCliente = cliente.gerarListaClientes()
            listaClientes = biblioDB.consultarBanco(sqlSelectCliente)
            cliente.verlistaClientes(listaClientes,"id")
            idEscolhidoCliente = msg.mensagemAlugarLivro("fraseI",listaClientes)
            if idEscolhidoCliente:
                aluguel.setIdCliente(idEscolhidoCliente)
                # visualizar lista de livros e escolher uma opção
                sqlSelectLivro = livro.gerarListalivros()
                listaLivro = biblioDB.consultarBanco(sqlSelectLivro)
                livro.verlistaLivro(biblioDB,listaLivro,"id")
                idEscolhidoLivro = msg.mensagemAlugarLivro("fraseII",listaLivro,True)
                if idEscolhidoLivro:
                    # vai mudar o status do livro para alugado
                    sqlLivroAlugado = livro.mudarStatusLivroAlugado(idEscolhidoLivro)
                    _ = biblioDB.manipularBanco(sqlLivroAlugado)
                    aluguel.setIdLivro(idEscolhidoLivro)
                    # outros dados do aluguel
                    sqlInsertAluguel = aluguel.cadastrarAluguel()
                    resultadoInsercao = biblioDB.manipularBanco(sqlInsertAluguel)
                    
                    msg.mensagemDeConfirmacao(resultadoInsercao)
                else:
                    msg.mensagemDeConfirmacao(idEscolhidoLivro)
            else:
                msg.mensagemDeConfirmacao(idEscolhidoCliente)

        case "3":
            livro.cadastrarLivro()
            sqlInsertAutor = livro.cadastrarAutor()
            _ = biblioDB.manipularBanco(sqlInsertAutor)
            sqlAutor = livro.gerarListaAutor()
            listaAutores = biblioDB.consultarBanco(sqlAutor)
            livro.setIdAutor(listaAutores)
            sqlInsertLivro = livro.sqlCadastrarLivro()
            resultadoInsercao = biblioDB.manipularBanco(sqlInsertLivro)
            msg.mensagemDeConfirmacao(resultadoInsercao)

        case "4":
            sqlSelectCliente = cliente.gerarListaClientes()
            listaClientes = biblioDB.consultarBanco(sqlSelectCliente)
            cliente.verlistaClientes(listaClientes,"completa")
            opcao = msg.alterarLista()
            if opcao == "Atualizar":
                cliente.verlistaClientes(listaClientes,"id")
                IdEscolhido = msg.mensagemAtualizar(listaClientes)
                if IdEscolhido:
                    sqlUpdateCliente = cliente.atualizar(IdEscolhido)
                    resultadoInsercao = biblioDB.manipularBanco(sqlUpdateCliente)
                    msg.mensagemDeConfirmacao(resultadoInsercao)
            elif opcao == "Deletar":
                cliente.verlistaClientes(listaClientes,"id")
                IdEscolhido = msg.mensagemDeletar(listaClientes)
                if IdEscolhido:
                    sqlDeleteCliente = cliente.deletar(IdEscolhido)
                    resultadoInsercao = biblioDB.manipularBanco(sqlDeleteCliente)
                    msg.mensagemDeConfirmacao(resultadoInsercao)
            else:
                pass 
        case "5":
            sqlSelectAluguel = aluguel.gerarListaAluguel()
            listaAluguel = biblioDB.consultarBanco(sqlSelectAluguel)
            aluguel.verlistaAluguel(listaAluguel,"completa")
            opcao = msg.alterarLista()
            if opcao == "Atualizar":
                aluguel.verlistaAluguel(listaAluguel,"id")
                IdEscolhido = msg.mensagemAtualizar(listaAluguel)
                if IdEscolhido:
                    sqlUpdateAluguel = aluguel.atualizar(IdEscolhido)
                    resultadoInsercao = biblioDB.manipularBanco(sqlUpdateAluguel)
                    msg.mensagemDeConfirmacao(resultadoInsercao)
            elif opcao == "Deletar":
                aluguel.verlistaAluguel(listaAluguel,"id")
                IdEscolhido = msg.mensagemDeletar(listaAluguel)
                if IdEscolhido:
                    sqlDeleteAluguel = aluguel.deletar(IdEscolhido)
                    resultadoInsercao = biblioDB.manipularBanco(sqlDeleteAluguel)
                    msg.mensagemDeConfirmacao(resultadoInsercao)
            else:
                pass 

        case "6":
            sqlSelectLivro = livro.gerarListalivros()
            listaLivro = biblioDB.consultarBanco(sqlSelectLivro)
            livro.verlistaLivro(biblioDB,listaLivro,"completa")
            opcao = msg.alterarLista()
            if opcao == "Atualizar":
                livro.verlistaLivro(biblioDB,listaLivro,"id")
                IdEscolhido = msg.mensagemAtualizar(listaLivro,True)
                if IdEscolhido:
                    sqlUpdateLivro = livro.atualizar(IdEscolhido)
                    resultadoInsercao = biblioDB.manipularBanco(sqlUpdateLivro)
                    msg.mensagemDeConfirmacao(resultadoInsercao)
            elif opcao == "Deletar":
                livro.verlistaLivro(biblioDB,listaLivro,"id")
                IdEscolhido = msg.mensagemDeletar(listaLivro,True)
                if IdEscolhido:
                    sqlDeleteLivro = livro.deletar(IdEscolhido)
                    resultadoInsercao = biblioDB.manipularBanco(sqlDeleteLivro)
                    msg.mensagemDeConfirmacao(resultadoInsercao)
            else:
                pass

print("Obrigado por usar a Biblioteca!")        
