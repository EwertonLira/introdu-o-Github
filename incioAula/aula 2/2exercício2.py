#  metodo for
numerosNoIntervalo = 0

for i in range(10):
    numero = float(input('Digite um número: '))
    if numero >=10 and numero <=50:
        numerosNoIntervalo += 1

print(f'A quantidade de números entre 10 e 50 é : {numerosNoIntervalo}')

