# Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 >>> 721

num = input("Insira um número inteiro: ")
numlist = []

for poslista in range((len(num))):
    for elemento in num:
        print(elemento,poslista)
        numlist[-poslista+(len(num))] = elemento 


def reverso(n):
    inverte = str(n)
    print (inverte[::-1])

def digitos(n):
    s = str(n)
    return len(s)

def potencia(base, expoente):
    resultado = 1
    for numero in range(1,expoente + 1):
        #base ** expoente = base * base (expoente vezes)
        resultado = resultado * base
    
    return resultado
