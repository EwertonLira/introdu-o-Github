# 5 Escreva uma função que receba como parâmetro um 
# número inteiro n e retorne uma lista com os n primeiros 
# números da sequência de Fibonacci. Em seguida, utilize 
# uma estrutura condicional para perguntar ao usuário se 
# ele deseja gerar a sequência de Fibonacci para outro número, 
# e utilize um laço de repetição para solicitar ao usuário 
# os novos valores de n, chame a função e imprima o resultado.

listaFibonacci = []
rodarWhile = True
rodarWhile1 = True

def fibonacci(valorEntrada):
    ultimo=1
    penultimo=1

    if (valorEntrada == 1) or (valorEntrada == 2):
        listaFibonacci.append(1)
    else:
        listaFibonacci.append(1)
        for numero in range((valorEntrada-1)):
            termo = penultimo + ultimo
            penultimo = ultimo
            ultimo = termo
            listaFibonacci.append(termo)
    
    return listaFibonacci

valorEntrada = int(input("quantos termos deseja encontrar: "))
print(f"os {valorEntrada} primeiros termos da sequência  ")
while rodarWhile:
    

    gerarOutroNumero = input("Tecle [S]sim ou [N]não: ")
    if gerarOutroNumero in ["s","S","sim","Sim","n","N","não","Não","nao","Nao"]:
        if gerarOutroNumero in ["s","S","sim","Sim"]:
            while rodarWhile1:
                listaFibonacci.clear()
                novoTermo = input("Insira a nova quantidade de termos: ")
                print(listaFibonacci(novoTermo))
                rodarWhile1 = False
        else:
            print("Obrigado por ter usado a nossa função")
            rodarWhile = False
    else:
        print("comando inválido")
