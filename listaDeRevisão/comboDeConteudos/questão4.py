# 4 Escreva uma função que receba como parâmetro uma 
# lista de números inteiros e retorne o número máximo na lista.
# Em seguida, utilize uma estrutura de repetição para solicitar 
# ao usuário uma lista de números inteiros, chame a função e 
# imprima o resultado. Se a lista estiver vazia, a função deve 
# retornar None e o programa deve imprimir uma mensagem informando 
# que a lista está vazia.

rodarWhile = True
rodarWhile1 = True
rodarWhile2 = True

listaDoUsuario = []

def MaiorNumero(lista):
    if lista:
        msg = max(lista)
    else:
        msg = None
    
    return msg

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
            rodarWhile = False
        except:
            print("entrada inválida, Somente numeros inteiros. preencha a lista novamente")
            listaDoUsuario.clear() # se ocorrer algum erro, a lista é limpa e começa novamente.

resultado = MaiorNumero(listaDoUsuario)
if resultado != None and resultado != 0:
    print("\no maior número da lista é",resultado,"\n")
else:
    print("A lista está vazia")