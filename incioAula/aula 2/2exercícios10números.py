#2exercícios10números.py

quantidade = 0

for i in range(10):
    numero = int(input('insira um número: '))

    if numero >= 10 and numero <=50:
        quantidade = quantidade + 1

print('Quantidade de números dentro do intervalo é', quantidade)
