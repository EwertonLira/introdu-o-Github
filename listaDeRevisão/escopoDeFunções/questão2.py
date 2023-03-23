# 2 Escreva um programa que solicite ao usuário um número e imprima se esse número é par ou ímpar.
# Crie uma função para determinar se um número é par e outra função para determinar se um número é ímpar.

def par(numero):
    if numero % 2 == 0 : # verificar se o número é divisível por 2 com resto zero, como todo número par
        msg = print(f"O número {numero} é par.")
    else:
        msg = print(f"{numero} não é par.")
    return msg 

def impar(numero):
    if numero % 2 != 0: #verifica se o número deixa resto ao ser dividido por 2, sendo um número impar.
        msg = print(f"O número {numero} é Impar.")
    else:
        msg = print(f"{numero} não é impar.")
    return msg 

rodaWhile = True
while rodaWhile: 
    try: # verificar se vai entrar somente dados núméricos.
        valorNumero = int(input("Insira um número: "))
        rodaWhile = False
    except:
        print("Insira somente números inteiros por favor.")

print()
impar(valorNumero)
par(valorNumero)
print()
