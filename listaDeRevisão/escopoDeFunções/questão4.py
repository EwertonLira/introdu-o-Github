# 4 Escreva uma função que calcule o fatorial de um número inteiro n. A função deve utilizar uma variável local
# para armazenar o resultado e uma estrutura de repetição para calcular o fatorial. Em seguida, utilize uma 
# variável global para contar quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada
# chamada.

# variáveis globais:
utilizacaoDeFuncao = 0
rodarwhile = True
rodarwhile1 = True

def fatorial(valor):
    global utilizacaoDeFuncao
    utilizacaoDeFuncao += 1
    
    valorFatorial = 1
    
    if valor == 0:
        valorFatorial = 1
    
    for numero in range(1,(valor + 1)):
        valorFatorial *= numero
    
    return valorFatorial

while rodarwhile:
    
    while rodarwhile1:
        try:
            valorDeEntrada = int(input("Insira um número natural: "))
            rodarwhile1 = False

        except:
            print("Por favor somente números naturais.")

    print(f"O fatorial de {valorDeEntrada}! é {fatorial(valorDeEntrada)}")
    
    print(f"A função fatorial() foi chamada {utilizacaoDeFuncao} vezes.")
    print(f"deseja usar a função novamente? [S]sim ou [N]não.")
    
    rodarwhile2 = True # variável global
    while rodarwhile2:
        SimOuNao = input(": ")
        if SimOuNao in ["s","S","sim","Sim","n","N","não","Não","nao","Nao"]:
            if SimOuNao in ["s","S","sim","Sim"]:
                valorDeEntrada = None
                rodarwhile1 = True
                rodarwhile2 = False

            else:
                rodarwhile2 = False
                rodarwhile = False

        else:
            print("tecle [S] ou [N] e aperte ENTER")