# Criar um programa calculadora
    # Receber dois números e uma operação(+,-,/,*)
    # Dependendo da operação escolhida, passa os números para uma das funções
    # No final imprime o resultado e a função escolhida

# Criar função para soma
# Criar função para subtração
# Criar função para multiplicação
# Criar função para divisão


def soma(numA,numB):
    numA, numB = float(numA), float(numB)
    SomaResultado = numA + numB
    return SomaResultado 

def subtracao(numA,numB):
    numA, numB = float(numA), float(numB)
    subtracaoResultado = numA - numB
    return subtracaoResultado

def multiplicacao(numA,numB):
    numA, numB = float(numA), float(numB)
    multiplicacaoResultado = numA * numB
    return multiplicacaoResultado

def divisao(numA,numB):
    if numB == 0:
        print("não é possível dividir por zero")
    numA, numB = float(numA), float(numB)
    divisaoResultado = numA / numB
    return divisaoResultado

def verificadorOperacao(valor):
    if valor in ["+","m","M","mais","Mais","soma"]:
        return True
    elif valor in ["-","s","S","menos","Menos"]:
        return True
    elif valor in ["*","mult","Mult","multiplicar","Multiplicar","vezes","Vezes"]:
        return True 
    elif valor in ["/","dividir","Dividir","D","d"]:
        return True
    else:
        return False

def verificadorNumero(valor):
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    contador = 0
    for i in valor:
        if i in numeros:
            contador += 1
            
    logica = len(valor) == contador
    return logica        

def main():
    num1 = ""
    while not (verificadorNumero(num1)):
        num1 = input("Insira um número: ")

    operacao = ""
    while not (verificadorOperacao(operacao)):
        operacao = input("Qual operação deseja fazer: ")

    num2 = ""
    while not (verificadorNumero(num2)):
        num2 = input("Insira um número: ")

    if operacao == soma():
        soma(num1,num2)

    soma()
    subtracao()
    divisao()
    multiplicacao()




    print("fim")

main()