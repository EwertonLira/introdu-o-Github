"""
1 Escreva um programa que imprima todos os números ímpares entre 1 e 50.
2 Escreva um programa que leia uma lista de números inteiros e imprima a média desses números.
3 Escreva um programa que solicite ao usuário um número e imprima a tabuada desse número até o valor 10.
4 Escreva um programa que solicite ao usuário um número e imprima todos os números primos menores que esse número.
"""
def questão1():
    numerosImpares = []
    for numero in range(1,50,2):
        numerosImpares.append(numero)
        
    print(numerosImpares)

def questão2():
    listaNumerosInteiros = []
    tamanhoDaLista = int(input("\tInsira o tamanho da lista: ")) # a quantidade de itens na lista
    for numeroInteiro in range(tamanhoDaLista):
        listaNumerosInteiros.append(int(input("insira um número inteiro: "))) # repete o números de vezes até prencher toda a lista
    
    media = sum(listaNumerosInteiros)/tamanhoDaLista
    print("A média da lista é: {}".format(media))

def questão3():
    valorDaTabuda = int(input("Insira o número da tabuada que deseja: "))
    
    for numero  in range(1,11):
        
        print(f'{numero:02}. {numero}x{valorDaTabuda} = {(numero*valorDaTabuda):02}') # o {:02} serve para prencher com zeros a esquerda do número.

def questão4():
    # essa parte serve para verificar se somente número inteiros vai entrar no input
    # caso não seja número intiro, vai ficar repetindo até conseguir um número inteiro
    try:
        valorDeEntrada = int(input("insira um número natural para saber se é primo: "))
    except:
        valorDeEntrada = 1
    
    while valorDeEntrada < 2:
       try:
        valorDeEntrada = int(input("insira um número natural maior 1: "))
       except:
           valorDeEntrada = 1

   # essa parte vai calcular um número se é primo ou não 
    for numero in range(2,valorDeEntrada):
        if valorDeEntrada % numero == 0: # pega o valor de entrada e dividi por todos os número, exceto por 1 e ele mesmo:
            print(f'O número {valorDeEntrada} não é primo.') # caso ocorra alguma divisão com resto zero, printa a mensagem e encerra a aplicação.
            break
    else:
       print(f"O número {valorDeEntrada} é primo!") #caso o for rode até o final ele cai no else, avisando que não teve nenhuma divisão com resto zero.
    


