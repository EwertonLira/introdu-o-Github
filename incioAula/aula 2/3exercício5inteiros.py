#3exercício5inteiros.py
lista = []
for i in range (5):
    lista = int(input('digite 5 números inteiros: '))
    print(lista)



menor = 0
for i in range(5):
    numero = int(input('Digite um inteiro: '))
    if menor == 0:
        menor = numero

    elif numero <=menor:
        menor = numero
    
print(' O menor número inserido foi:',menor)

# zero não conta como menor!