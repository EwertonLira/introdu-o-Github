# 1 Escreva um programa que solicite ao usuário dois números e imprima a soma, a subtração, a multiplicação e a 
# divisão desses números. Crie funções separadas para cada operação matemática.

def soma(numero1, numero2):
    msg = F"soma: {numero1} + {numero2} = {numero1 + numero2}"
    return print(msg)

def subtração(numero1, numero2):
    msg = F"subtração: {numero1} - {numero2} = {numero1 - numero2}"
    return print(msg)

def multiplicação(numero1, numero2):
    msg = F"multiplicação: {numero1} x {numero2} = {numero1 * numero2}"
    return print(msg)

def divisão(numero1, numero2):
    try:
        msg = F"Divisão: {numero1} ÷ {numero2} = {numero1 / numero2}"
        return print(msg)
    except ZeroDivisionError:
        print("não é possível dividir por zero")

rodaWhile = True
while rodaWhile: 
    try: # verificar se vai entrar somente dados núméricos.
        priNumero = float(input("Insira o 1º número: "))
        segNumero = float(input("Insira o 2º número: "))
        rodaWhile = False
    except:
        print("Insira somente números por favor.")

print() #pular uma linha
soma(priNumero,segNumero)
subtração(priNumero,segNumero)
multiplicação(priNumero,segNumero)
divisão(priNumero,segNumero)
print()

