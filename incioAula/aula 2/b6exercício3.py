# 6.Ler do teclado um número inteiro e imprimir se ele é primo ou não.

numero = int(input("insira um número natural maior 1: "))

while numero < 2:
     numero = int(input("insira um número natural maior 1: "))

verificador = False
for i in range(2,numero):
    if numero % i == 0:
        verificador = True 

if verificador:
     print(f'O número {numero} não é primo.')
else:
    print(f"O número {numero} é primo!")

###############################################
# numero = int(input("insira um número natural maior 1: "))

# while numero < 2:
#     numero = int(input("insira um número natural maior 1: "))

# if numero in [2,3,5,7]:
#     print(f"O número {numero} é primo!")
# else:
#     numeroTexto =str(numero)
#     logica1 = numeroTexto[-1] in ["0","2","4","5","6","8",]
#     if logica1 == True:
#         print(f'O número {numero} não é primo.')
#     else:
#         MetadeNum = int((numero +1)/2)
#         verificador = None
#         for i in range(2,MetadeNum):
#             if numero % i == 0:
#                 verificador = True
        
# if verificador:
#     print(f'O número {numero} não é primo.')
# else:
#    print(f"O número {numero} é primo!")


###################################################################################
# numero = int(input("Digite um número inteiro: "))

# contador = 0

# for i in range(1,numero + 1):

#     if numero % i == 0:
#         contador = contador + 1
#         print(contador,"-",i)

# if contador <=2:
#     print(numero, "É primo")
# else:
#     print(numero, "não é primo")