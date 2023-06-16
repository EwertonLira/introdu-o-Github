
lista = ['abc','xyz','aba',1221, "a"]

contador = 0

for nome in lista:
    comparador = str(nome)
   
    if comparador[0] == comparador[-1] and len(comparador) >= 2:
        print(comparador)
        contador += 1

print('numero de termos',contador)
