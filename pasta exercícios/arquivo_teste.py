lista = ['banana','acerola','abacaxi', 'limão', 'uva']

def numerolista():
    for index, valor in enumerate(lista,start=1):
        print(index, valor )

numerolista()

lista.append('kiwi')
print("")
numerolista()



