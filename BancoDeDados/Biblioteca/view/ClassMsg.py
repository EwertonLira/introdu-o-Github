
class Msg:
    def __init__(self):
        pass

    def visualizarMenu(self):
        print('''
        📙📗 Blioteca 📘📕

Sistema de gerenciamento de Biblioteca:
Escolha uma das opções[] abaixo e tecle [Enter↵]

[1]✍️👪 Cadastro de clientes
[2]✍️🧾 Cadastro de aluguéis
[3]✍️📚 Cadastro de livros
[4]👀️👪 Visualizar lista de Clientes
[5]👀🧾 visualizar lista de aluguéis
[6]👀📚️ Visualizar lista de livros
[0]🚪 Sair
    ''')

        op = input(": ")
        if op in "1¬2¬3¬4¬5¬6¬0":
            pass
        else:
            print("comando inválido, tente novamente")
            input("aperte [Enter↵] para continuar")
        
        return op

    def mensagemDeConfirmacao(self,resultado):
        if resultado:
            print("Registro efetuado!")
            input("aperte [Enter↵] para continuar")
        else:
            print("O registro falhou")
            input("aperte [Enter↵] para continuar")

    def alterarLista(self):
        
        op = "rodarWhile"
        while not(op in "1|2|0"): 
        
            print("""
Deseja fazer alteração na lista visualizada?
Digite [1]Atualizar, [2]Deletar ou [0]sair.
    
    [1] Atualizar 
    [2] Deletar
    [0] sair
    """)
            op = input(": ")
            match op:
                case "1":
                    opEscolhida = "Atualizar"
                case "2":
                    opEscolhida = "Deletar"
                case "0":
                    opEscolhida = False
                case _:
                        print("comando inválido, tente novamente")
                        input("aperte [Enter↵] para continuar")
        
        return opEscolhida
    
    def mensagemAtualizar(self,lista,tipoLivro=False):
        verificarID = self._pegarIdLista(lista,tipoLivro)

        opcao = "rodarWhile"
        while not(opcao in verificarID):
            print("Digite o ID do item da lista a ser atualizado:")          
            try:
                opcao = int(input(": "))                
                if opcao in verificarID:
                    pass
                else:
                    print("ID não encontrado")
                    print("Voltando ao menu principal")
                    input("aperte [Enter↵] para continuar")
                    opcao = False
                    break
            except:
                print("comando invalido. Tente novamente")
   
        return opcao
    
    def _pegarIdLista(self,lista,TipoLivro = False):
        if TipoLivro:
            indice = 5
            # print(lista)
            # print("acima original")
            # lista = lista[0]
            # print("teste de vericar",lista )
            # print(indice)
        else:
            indice = 6
    
        verificarID = []
        for id in lista:
            verificarID.append(id[0])
        
        verificarIdATivo = []
        for cliente in lista:
            if cliente[indice] == "desativado" or cliente[indice] == "alugado" :
                verificarIdATivo.append(cliente[0])

        verificarID = set(verificarID)
        verificarIdATivo = set(verificarIdATivo)

        idValidos = verificarID - verificarIdATivo
        listaIdvalidos = list(idValidos)

        return listaIdvalidos


    def mensagemDeletar(self,lista,TipoLivro=False):
        verificarID = self._pegarIdLista(lista,TipoLivro)

        opcao = "rodarWhile"
        while not(opcao in verificarID):
            print("Digite o ID do item da lista a ser apagado:")          
            try:
                opcao = int(input(": "))                
                if opcao in verificarID:
                    pass
                else:
                    print("ID não encontrado")
                    print("Voltando ao menu principal")
                    input("aperte [Enter↵] para continuar")
                    opcao = False
                    break
            except:
                print("comando invalido. Tente novamente")
   
        return opcao

    def mensagemAlugarLivro(self,frases, lista,TipoLivro = False):
        idValidos = self._pegarIdLista(lista,TipoLivro)

        loop = "rodarWhile"
        while loop != "parar":
            match frases:
                case "fraseInicial":
                    print("\nPrencha os campos para efeturar um aluguel\n")
                    opcao = False
                    loop = "parar"
                case "fraseI":
                    try:
                        opcao = int(input("\nEscolha o ID do Cliente: "))             
                        if opcao in idValidos:
                            loop = "parar"
                        else:
                            print("ID não encontrado")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
                case "fraseII":
                    try:
                        opcao = int(input("\nEscolha o ID do livro: "))                
                        if opcao in idValidos:
                            loop = "parar"
                        else:
                            print("ID não encontrado")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
        return opcao