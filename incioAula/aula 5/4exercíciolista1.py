listaNumeros = [2,14,14,21,10]

comparador = listaNumeros[0]
for i in listaNumeros:
    if i < comparador:
        comparador = i

print(min(listaNumeros))
print(listaNumeros)
print("O menor número da listas é: ", comparador)

