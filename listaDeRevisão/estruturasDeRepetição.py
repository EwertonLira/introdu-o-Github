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
    # essa parte serve para verificar se somente número natural vai entrar no input
    # caso não seja número natural, vai ficar repetindo até conseguir um número natural
    try:
        valorDeEntrada = int(input("insira um número natural: "))
    except:
        valorDeEntrada = 1
    
    while valorDeEntrada < 2:
       try:
        valorDeEntrada = int(input("Por favor insira um número natural: "))
       except:
           valorDeEntrada = 1

   # essa parte vai calcular um número se é primo ou não 
    listaOrdenada = set() # criamos dois conjuntos pois conjuntos não permite variáveis repetidas. um conjunto de numeros naturais e outros de não primos.
    listaNaoPrimo = set()

    for numero in range(valorDeEntrada): # esse for serve para mostrar cada número até o número inserido pelo usuário.
        novoValorDeEntrada = valorDeEntrada - numero
            
        for cadaNumero in range(2,novoValorDeEntrada): # nesse for faz a divisão de cada número pelos numeros com valor abaixo dele para saber se não é primo.
            if novoValorDeEntrada % cadaNumero == 0:
                listaNaoPrimo.add(novoValorDeEntrada)
        
    for numeracao in range(2,(valorDeEntrada +1)): # cria uma lista de números do 2 até o numero escolhido pelo usuário
        listaOrdenada.add(numeracao)
    
    listaPrimos =  listaOrdenada - listaNaoPrimo # aqui o conunto "listaOrdenada" diferença"-" listaNaoPrimo vai mostraro que somente está contindo na listaOrdenada(somente os primos)

    print("Números primos até o",valorDeEntrada)
    print(listaPrimos)#mostra o conjunto na tela

