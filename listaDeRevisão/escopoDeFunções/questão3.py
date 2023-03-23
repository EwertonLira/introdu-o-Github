# 3 Escreva uma função que receba uma lista de números inteiros como parâmetro e retorne a média dos números. 
# A função deve verificar se a lista está vazia e retornar None caso esteja. Em seguida, utilize uma variável 
# global para contar quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada chamada.

#variáveis globais
listaDoUsuario = [] #lista a ser preenchida pelo usuário
rodarWhile = True  # inicia o while
rodarWhile1 = True 
rodarWhile2 = True 
rodarWhile3 = True
vezesUtilizado = 0 #indica quantas vezes o progrma foi utilizado

def mediaLista(lista):  
    global vezesUtilizado #utilizando a várial global para guardar o número de vezes que o programa foi chamado.
    vezesUtilizado += 1
    if lista:                         # listas com algum elemento retornam True então colocamos a operção de média no if.
        media = sum(lista)/len(lista)
    else:                             # lista vazias retornam False então colocamos o valor None no else.
        media = None
    return media

while rodarWhile: # esse while vai fazer o o programa repetir caso o usuário decida usar denovo.
    while rodarWhile1:
        try: # esse try verifica se vai entra somente números na escolha do tamanho da lista
            tamanhoDaLista = int(input("\nInsira quantos itens a lista vai ter: "))
            rodarWhile1 = False # se ocorrer nenhum erro, o while para de rodar
        except Exception as error:
            print("entrada inválida, Somente numeros inteiros.") # se ocorrer algum erro ele adverte com essa mensagem e roda novamente o programa.

    while rodarWhile2: # esse while serve para o usuário inserir cada numero na lista que ele criou.
        try:
            for itemDaLista in range(tamanhoDaLista):
                listaDoUsuario.append(int(input(f"insira o {itemDaLista +1}º item da lista de {tamanhoDaLista}: ")))
            rodarWhile2 = False
        except:
            print("entrada inválida, Somente numeros inteiros. preencha a lista novamente")
            listaDoUsuario.clear() # se ocorrer algum erro a lista e limpa e começa novamente.

    ResultadoDaFuncao = mediaLista(listaDoUsuario) # aqui a função é chamada.
    if ResultadoDaFuncao != None and ResultadoDaFuncao != 0: # se o resultado diferente de zero ou None ele mostra o resultado
        print(f"\nA média da sua lista é {ResultadoDaFuncao:.2f}")
    elif ResultadoDaFuncao == 0: # se o resultado for zero ou none ele vai mostra: None
        print(None)
    else:
        print(ResultadoDaFuncao)

    print(f"\nO programa foi utilizado {vezesUtilizado} vezes pelo usuário.") # essa parte serve para mostrar quantas vezes o programa foi utilizado e serve para reiniciar o programa caso queira.
    print("Deseja usar novamente o programa?")
    while rodarWhile3:
            repetirScript = input("[S]sim ou [N]não: ") 
            if repetirScript in ["s","S","sim","Sim","n","N","não","Não","nao","Nao"]: # verificar se entrou um dado válido.
                rodarWhile3 = False
            else:
                print("digite sim ou não ou tecle [S] ou [N] e aperte ENTER")
                
    if repetirScript in ["s","S","sim","Sim"]: #caso o usurio queira usar novamente, lipamos a lista e deixamos os whiles True novamente.
        listaDoUsuario.clear()
        rodarWhile1 = True
        rodarWhile2 = True
        rodarWhile3 = True
    else:
        rodarWhile = False # caso não queria fechamos o programa  