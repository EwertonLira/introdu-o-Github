vezesUtilizado = 0
lista = [1,2,3]
def mediaLista(lista):  
    global vezesUtilizado
    print('a',vezesUtilizado)
    vezesUtilizado += 1
    print('b',vezesUtilizado)
    if lista:                         # listas com algum elemento retornam True então colocamos a operção de média no if.
        media = sum(lista)/len(lista)
    else:                             # lista vazias retornam False então colocamos o valor None no else.
        media = None
    return media

print(mediaLista(lista))
print(vezesUtilizado)
