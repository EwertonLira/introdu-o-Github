# Q.1 Construa um algoritmo para ler um número inteiro, positivo de três dígitos, e gerar outro número formado pelos dígitos invertidos do número lido. 
#  Ex: 
# NumeroLido = 123 
# NumeroGerado = 321 
# Dica: Observe os resultados das funções Quociente e Resto de um número por 10.

numero = int(input("insira um número de 3 digitos: "))

dig1 = numero // 100
restoDig1 = numero % 100

dig2 = restoDig1 // 10
restoDig2 = restoDig1 % 10

dig3 = restoDig2 // 1


numeroInv = "".join([str(dig3),str(dig2),str(dig1)])

print(f'\nO inverso do número {numero} é:\n>>>\t{numeroInv}\t<<<\n')
