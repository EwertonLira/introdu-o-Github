# 1. Escreva uma função que receba como parâmetro uma lista de 
# números inteiros e retorne a soma dos números pares na lista. 
# Em seguida, utilize um laço de repetição para solicitar ao 
# usuário uma lista de números inteiros, chame a função e imprima
# o resultado.

numerosInteiros = [10,15,20,25,30,35,40,45,50,17,21,35,42,52,65,70,85,95,90,120,125]
listaDoUsuario = []
rodarWhile = True
rodarWhile1 = True
rodarWhile2 = True

def somaPares(lista):
    valorTotalPares = 0
    
    for numero in lista:
        if numero % 2 == 0:
            valorTotalPares += numero
    
    return valorTotalPares

print("\n",numerosInteiros)
print(f"A soma dos número pares da lista acima é: {somaPares(numerosInteiros)}")

while rodarWhile: # esse while vai fazer o o programa repetir caso o usuário decida usar denovo.
   
    while rodarWhile1:
       
        try: # esse try verifica se vai entra somente números na escolha do tamanho da lista
            print("\nCrie uma nova lista:")
            tamanhoDaLista = int(input("Insira quantos itens a lista vai ter: "))
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
            listaDoUsuario.clear() # se ocorrer algum erro, a lista é limpa e começa novamente.
    
    print(listaDoUsuario)
    print(f"A soma dos número pares da sua lista é: {somaPares(listaDoUsuario)}")
    rodarWhile = False