
for i in range(5):
    numero = int(input("insira um número inteiro: "))

    if i == 0:
        menor = numero
    else:
        if numero < menor:
            menor = numero
print("O menor número foi", menor)
