# Q.2 Elabore um algoritmo que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 reais.
Saque = []
notasValor = [100, 50, 20, 10, 5, 2, 1]

Saque = int(input("insira o valor do saque: "))

for i, valor in enumerate(notasValor):
    print(i, valor)
    notasQtd[i] = notasSaque[i] // notasValor[i]
    notasSaque.append( notasSaque[i] % notasValor[i] )

print(notasSaque,notasValor,notasQtd)   

# notas100 = saque // 100
# resto100 = saque // 100