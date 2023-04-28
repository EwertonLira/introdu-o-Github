import json


def pegarListaAtualizada():

    with open("1 aula/funcionario.json", 'r') as funcionariosJson:
        lista = json.load(funcionariosJson)

    return lista

def verFuncionarios():

    listaFuncionarios = pegarListaAtualizada()

    print("Lista de Funcionários: ")

    print("Nome | CPF | Salario | Cargo | Departamento")

    for funcionario in listaFuncionarios:

        print(
            f'{funcionario["nome"]} | {funcionario["cpf"]} | {funcionario["salario"]} | {funcionario["cargo"]} | {funcionario["departamento"]}')

    input()

def inserirFuncionario():

    funcionario = {}

    # for dado in funcionario.keys:

    #     insercao = input(f"Insira o {dado}")

    #     funcionario[dado] = insercao

    print("Inserir Novo Funcionário:")

    nomeFuncionario = input("Insira o nome do Funcionário: ")
    cpfFuncionario = input("Insira o cpf do Funcionario: ")
    salarioFuncionario = input("Insira o salario do Funcionario: ")
    cargoFuncionario = input("Insira o cargo do Funcionario: ")
    departamentoFuncionario = input("Insira o departamento do Funcionario: ")

    funcionario["nome"] = nomeFuncionario
    funcionario["cpf"] = cpfFuncionario
    funcionario["salario"] = float(salarioFuncionario)
    funcionario["cargo"] = cargoFuncionario
    funcionario["departamento"] = departamentoFuncionario

    listaFuncionarios = pegarListaAtualizada()
    listaFuncionarios.append(funcionario)

    with open("1 aula/funcionario.json", 'w') as funcionariosJson:
        json.dump(listaFuncionarios, funcionariosJson, indent=2)

def removerFuncionario():
    listaFuncionarios = pegarListaAtualizada()

    print("Lista de Funcionários: ")

    print("Nome | CPF | Salario | Cargo | Departamento")

    for posicao, funcionario in enumerate(listaFuncionarios):

        print(
            f'{posicao}. {funcionario["nome"]} | {funcionario["cpf"]} | {funcionario["salario"]} | {funcionario["cargo"]} | {funcionario["departamento"]}')

    item  = int(input("qual funcionário deseja remover: "))
    
    listaFuncionarios = pegarListaAtualizada()
    listaFuncionarios.pop(item)
    with open("1 aula/funcionario.json", 'w') as funcionariosJson:
        json.dump(listaFuncionarios, funcionariosJson, indent=2)

def atualizarFuncionario():
    
    listaFuncionarios = pegarListaAtualizada()

    print("Lista de Funcionários: ")

    print("Nome | CPF | Salario | Cargo | Departamento")

    for posicao, funcionario in enumerate(listaFuncionarios):

        print(
            f'{posicao}. {funcionario["nome"]} | {funcionario["cpf"]} | {funcionario["salario"]} | {funcionario["cargo"]} | {funcionario["departamento"]}')

    item  = int(input("qual funcionário deseja atualizar: "))

    funcionario = {}

    # for dado in funcionario.keys:

    #     insercao = input(f"Insira o {dado}")

    #     funcionario[dado] = insercao
    
    nomeFuncionario = input("Insira o nome do Funcionário: ")
    cpfFuncionario = input("Insira o cpf do Funcionario:")
    salarioFuncionario = input("Insira o salario do Funcionario:")
    cargoFuncionario = input("Insira o cargo do Funcionario:")
    departamentoFuncionario = input("Insira o departamento do Funcionario:")

    funcionario["nome"] = nomeFuncionario
    funcionario["cpf"] = cpfFuncionario
    funcionario["salario"] = float(salarioFuncionario)
    funcionario["cargo"] = cargoFuncionario
    funcionario["departamento"] = departamentoFuncionario

    listaFuncionarios.pop(item)
    listaFuncionarios.insert(item,funcionario)

    with open("1 aula/funcionario.json", 'w') as funcionariosJson:
        json.dump(listaFuncionarios, funcionariosJson, indent=2)

while True:

    print('''
    Bem vindo a Empresa XYZ
    Menu:
    1. Ver Funcionários
    2. Inserir Funcionário
    3. atualizar Funcionário
    4. remover Funcionário
    0. Sair
    
    ''')

    op = input("Escolha uma opção: ")

    match op:
        case "1":
            verFuncionarios()
        case "2":
            inserirFuncionario()
        case "3":
            atualizarFuncionario()
        case "4":
            removerFuncionario()
        case "0":
            print("Saindo do Programa...")
            break
