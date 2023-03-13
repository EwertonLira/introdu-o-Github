# Tipos de Dados

# 1. Escreva um programa que solicite ao usuário um número inteiro e imprima o dobro desse número.

# 2. Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área desse círculo.

# 3. Escreva um programa que solicite ao usuário seu nome e idade e imprima uma mensagem personalizada com essas informações.


def questão1 ():
    numeroInteiro = int(input(f"Por favor insira um número inteiro: "))
    print(f"o dobro de {numeroInteiro} é {numeroInteiro * 2}")

def questão2():
    raioCirculo = float(input("Por favor Insira o valor do Raio: "))
    areaDoCirculo = 3.14159265 * (raioCirculo**2) # 3,14159265 valor de pi com 8 casas decimais.
    print(f"A área do Círculo é igual a: {areaDoCirculo:.2f}") #o Valor vai ser mostrado com apenas 2 casas decimais {_:.2f}

def questão3():
    # Fonte de dados:
    # https://educador.brasilescola.uol.com.br/estrategias-ensino/faixa-etaria-populacao-brasileira.htm#:~:text=Jovens%20%E2%80%93%20do%20nascimento%20at%C3%A9%20aos,anos%20de%20idade%20ou%20mais.
    
     
    nome = input("Insira seu nome: ")
    idade = int(input("Insira sua idade: "))

    if idade <= 19 and idade >= 0:
        faixaetaria = "jovem"
    elif idade <= 59 and idade >= 20:
        faixaetaria = "adulto"
    elif idade <= 140  and idade >= 60:
        faixaetaria = "idoso"
    else:
        faixaetaria = "incerta"
    
    print(f"""
    Olá {nome} com sua idade de {idade} anos
    a sua faixa etária é {faixaetaria}.\n""")

questão3()

