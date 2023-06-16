# Enunciado: faça um programa que escolha um número aleatório entre 1 e 100, 
# e peça para o usuário inserir um valor como palpite. O programa deve continuar 
# até acertar e deve informar se está maior ou menor que o valor sorteado.
import random
ale = 1
pite = 0
while pite != ale:
    pite = int(input("insira um número: "))
    ale = random.randint(1, 100)
    print(f'Seu palpite foi {pite} o número sorteado foi:{ale}')

print(f'Parabens você acertou o número sorteado!\nNúmero: {pite}')
