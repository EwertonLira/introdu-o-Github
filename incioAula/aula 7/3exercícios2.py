# Faça uma função que receba uma lista de números armazenados de forma crescente, e
# dois valores ( limite inferior e limite superior), e exiba a sublista cujos elementos são
# maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

def contarString(valor):
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    contador = 0
    for i in valor:
        if i in numeros:
            contador += 1
    
    logica1 = contador == len(valor)
    return logica1

def subconjnto(lista,menor,maior):
    novaLista = []
    lista
    for i in lista:
        if i >= menor and i <= maior:
            novaLista.append(i)
    
    novaLista.sort()
    return novaLista    

lista = []

a = True
while type("fim") != type(a):
    a = input("insira os valores númericos da lista e aperte qualquer letra para parar: ")
    if contarString(a):
        lista.append(int(a))
        a = True
    else:
        a = "fim"

b = int(input("Insira o menor valor: "))
c = int(input("Insira o Maior valor: "))

print(subconjnto(lista,b,c))

