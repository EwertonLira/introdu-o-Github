
listaNumeros = []
for i in range(5):
   listaNumeros.append(int(input("Digite um inteiro: ")))

comparador = listaNumeros[0]
for i in range(len(listaNumeros)):
    if listaNumeros[i] > comparador:
        comparador = listaNumeros[i]

print(max(listaNumeros))
print(listaNumeros)
print("O maior número da listas é: ", comparador)
