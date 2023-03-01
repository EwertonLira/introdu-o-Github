lista = ['banana','acerola','ACerola','ABacaxi', 'limão', 'uva'] # prioridade é as palavras em maiúscualas seguindo pela ordem alfabética.

print(min(lista))

def numerolista():
    for i, valor in enumerate(lista,start=0):
        ix, iy = i -1 , i 
        print(lista[ix] +' '+ lista[iy])

numerolista()

lista.append('kiwi')
print("")
numerolista()





