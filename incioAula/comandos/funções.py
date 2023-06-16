# def hello(meuNome, sobreNome,idade):
#     print('Hello',meuNome, sobreNome , idade)


# tupla = ("Fábio","Martins",20)

# hello("Ewerton","Lira", 20)
# hello("Pedro","Tiago",2)
# hello(idade=20,meuNome="Ewerton",sobreNome="Lira")
# hello(tupla[0],tupla[1],tupla[2])

# def teste(num1,num2,op):
#     numero1 = float(num1)
#     numero2 = float(num2)

#     if op == "+":
#         return numero1 + numero2
#     elif op == "-":
#         return numero1 - numero2
#     else:
#         return "escolha outro operador"
    
def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    
    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))

    return salario
       

# qtd_horas = input("insira as horas trabalhadas: ")
# valor_hora = input("insira o valor da hora trabalhada: ")

# print(f'\nvalor a ser pago:\t{calcular_pagamento(qtd_horas,valor_hora)}')

def calculoImc(peso, altura):
    print(peso / altura ** 2)

calculoImc(peso = 75, altura = 1.68)
calculoImc(80,1.72)


