lista = ['banana','acerola','abacaxi', 'limão', 'uva']

def numerolista():
    for i, valor in enumerate(lista,start=1):
        ix, iy = i + 1 , i + -1
        print(valor[ix] + valor[iy])

numerolista()

lista.append('kiwi')
print("")
numerolista()




