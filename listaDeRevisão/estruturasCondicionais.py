# 1. Escreva um programa que solicite ao usuário um número e imprima se ele é positivo, negativo ou zero.

# 2. Escreva um programa que leia o nome e a idade de uma pessoa e imprima uma mensagem personalizada com base na idade. 
# Se a idade for menor que 18 anos, imprima "Você é menor de idade". 
# Se a idade estiver entre 18 e 65 anos, imprima "Você é adulto". Caso contrário, imprima "Você é idoso".

#  3. Escreva um programa que solicite ao usuário a nota de um aluno em uma prova e imprima 
# a mensagem "Aprovado" se a nota for maior ou igual a 7, "Reprovado" se a nota for menor que 5 
# e "Recuperação" se a nota estiver entre 5 e 7.
 
# 4. Escreva um programa que solicite ao usuário a idade e o sexo de uma pessoa e imprima uma mensagem 
# personalizada com base nas seguintes condições:
# Se a pessoa for do sexo feminino e tiver menos de 25 anos, imprima "Você é uma jovem mulher".
# Se a pessoa for do sexo feminino e tiver 25 anos ou mais, imprima "Você é uma mulher adulta".
# Se a pessoa for do sexo masculino e tiver menos de 25 anos, imprima "Você é um jovem homem".
# Se a pessoa for do sexo masculino e tiver 25 anos ou mais, imprima "Você é um homem adulto".

def questão1():
       
    valorEntrada = float(input("Insira um número qualquer: "))
    if valorEntrada == 0: # verifica se igual a zero
        print("O número é igual a Zero.")
    elif valorEntrada > 0: # verifica se maior que zero
        print("O número é positivo.")
    else: # mostra os resultados negativos.
        print("O número é negativo")

def questão2():

    nome = input("Insira o seu nome: ")
    idade = int(input("Insira a sua idade: "))
    # vai reficar em qual condição a idade dele se encaixa e vai retornar uma mensagem.
    if idade < 18:
        print(f"{nome.capitalize()} você é menor de idade") 
    elif idade >= 18 and idade < 65:
        print(f"{nome.capitalize()} você é adulto")
    else:
        print(f"{nome.capitalize()} você é idoso")
    
def questão3():
    
    notaAluno = float(input("Digite a Nota do aluno: "))

    if notaAluno >= 7: # verificar se maior que 7 a nota do aluno.
        print("Aprovado")
    elif notaAluno >= 5 and notaAluno < 7: # verifica se a nota do aluno está entre 5 e 7.
        print("Recuperação")
    else: # A nota do aluno é menor que 5 caso chegue aqui.
        print("Reprovado")



