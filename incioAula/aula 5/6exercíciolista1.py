

lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

novaLista = []

for tupla in lista:
    novaLista.append(tupla[::-1])

novaLista.sort()

lista.clear()

for tupla in novaLista:
    lista.append(tupla[::-1])

print(lista)



