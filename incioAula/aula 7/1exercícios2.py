def dezporcento(valorDaConta):
   gorjeta = valorDaConta / 10
   return gorjeta

conta = float(input('insira o valor da conta: '))
print(f'A gorjeta é: {dezporcento(conta)}')

# def calcularGorjeta(valorConta):
    
#     gorjeta = float(valorConta) * 0.1

#     return gorjeta

# conta = input("Digite o valor da conta: ")
# gorjetaConta = calcularGorjeta(conta)

# totalConta = float(conta) + gorjetaConta

# print("Valor da gorjeta R$", gorjetaConta)
# print("Valor total da conta R$", totalConta)