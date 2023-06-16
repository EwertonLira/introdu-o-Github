# Escreva um programa q contenha uma função que  imprima os numeros de 0 a um numero escolhido. 
#Para multiplos de 3 imprima "Ninho" na frente do numero 
#e para os multiplos de cinco imprima "desenvolvedor". 
#Para números que sao multiplos de tres e cinco imprima "Nindo de Desenvolvedores"
#para o restante dos números imprima Senac

numEscolhido = int(input("Insira um número inteiro: "))

for i in range((numEscolhido + 1)):
    if i == 0:
        print("Senac",i)
    elif (i % 5) == 0 and (i % 3) == 0:
        print("Ninho de Desenvolvedores",i)
    elif (i % 3) == 0:
        print("Ninho",i)
    elif (i % 5) == 0:
        print("Desenvolvedor",i)
    elif (i % 5) == 0:
        print("Desenvolvedor",i)
    else:
        print("Senac",i)   