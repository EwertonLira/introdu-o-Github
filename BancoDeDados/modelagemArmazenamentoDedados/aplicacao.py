import json
from os import system
caminho = "Aula01.json"

def abrirArquivo():
    with open(caminho, "r") as arquivoJson:
        bancoDeDadosJson = json.load(arquivoJson)

    return bancoDeDadosJson
       
def menuDeopções():
    # menu onde aparece o texto e o comando de entrada de dados
    while True:
        print(f""" 
        Sistema de gerenciamento da Empresa 
                        ABC 
                    
        [1] Listar Funcionários
        [2] Listar Departamentos
        [3] Informações do Funcionário
        [4] Informações do Departamento
        [0] Sair
        
        """)
        try:
            opcao = int(input(": "))
            system("cls")
            if opcao in [0,1,2,3,4]:
                return opcao
            else:
                print("Comando Inválido. Tente Novamente")
                input("\nPressione ENTER para continuar")
        except:
            print("Comando Inválido. Tente Novamente")
            input("\nPressione ENTER para continuar")

def RodarOpçãoDoMenu(opçãoEscolhida):
    # vai rodar a opção escolhida
    bancoDeDadosJson = abrirArquivo()
    
    match opçãoEscolhida:
        case 1:
            mostrarListaFuncionários(bancoDeDadosJson)
            input("\nPressione ENTER para continuar")
            system("cls")
        case 2:
            mostrarListaDepartamento(bancoDeDadosJson)
            input("\nPressione ENTER para continuar")
            system("cls")
        case 3:
            mostrarInformaçõesFuncionários(bancoDeDadosJson)
            input("\nPressione ENTER para continuar")
            system("cls")
        case 4:
            mostrarinformaçõesDepartamento(bancoDeDadosJson)
            input("\nPressione ENTER para continuar")
            system("cls")
        case 0:
            comando = saidaDoMenu()
            return comando

def mostrarListaFuncionários(bancoDeDadosJson):
    # função que mostra a lista de todos os funcionários.

    print("\nlista de funcionário cadastrados:")
    for elemento in bancoDeDadosJson[["funcionarios"][0]]:
        print(f"""ID: {elemento["id_funcionario"]} Nome: {elemento["id_nome"]}""")

def mostrarListaDepartamento(bancoDeDadosJson):
    # função que mostra a lista de todos os departamentos
    print("\nDepartamentos ativos")
    for elemento in bancoDeDadosJson[["departamento"][0]]:
        print(f"""
        ID do departamento: {elemento["id_departamento"]}
        ID do cargo: {elemento["id_cargo"]}""")

def mostrarInformaçõesFuncionários(bancoDeDadosJson):
    # procurar o nome no banco de dados do json
    naoEncontrado = True
    print("Insira o ID do funcionário ou nome")

    while True:
        valorDeEntrada = input(": ")
        system("cls")
        for funcionario in bancoDeDadosJson[["funcionarios"][0]]:
            
            id = str(funcionario["id_funcionario"])
            nome = funcionario["id_nome"]
            
            nome = nome.upper()
            valorDeEntrada = valorDeEntrada.upper()
            
            if nome == valorDeEntrada or id == valorDeEntrada:
                print(f"""
                ID: {funcionario["id_funcionario"]}
                Nome: {funcionario["id_nome"]}
                CPF: {funcionario["id_cpf"]}
                Departamento: {funcionario["id_departamento"]}""")
                naoEncontrado = False
        
        if naoEncontrado:
            print("funcionário não encontrado, verfique as informações e tente novamente.")
        
        break    

def mostrarinformaçõesDepartamento(bancoDeDadosJson):
    # mostra as informações do departamento
    naoEncontrado = True
    print("Insira o ID do departamento ou cargo")

    while True:
        valorDeEntrada = input(": ")
        system("cls")
        for departamento in bancoDeDadosJson[["departamento"][0]]:
            
            id = str(departamento["id_departamento"])
            cargo = departamento["id_cargo"]
            
            cargo = cargo.upper()
            valorDeEntrada = valorDeEntrada.upper()
            
            if cargo == valorDeEntrada or id == valorDeEntrada:
                print(f"""
                Dados do departamento:
                ID: {departamento["id_departamento"]}
                cargo: {departamento["id_cargo"]}""")
                naoEncontrado = False

                print("lista de funcionários do Departamento")
                for funcionario in bancoDeDadosJson[["funcionarios"][0]]:
                    idFKFun = str(funcionario["id_departamento"])
                    
                    if id == idFKFun:
                        print(f"""ID: {funcionario["id_funcionario"]} Nome: {funcionario["id_nome"]}""")
                        
        if naoEncontrado:
            print("Departamento não encontrado, verfique as informações e tente novamente.")
        
        break

def saidaDoMenu():
    print("""Você tem certeza que deseja sair?
    tecle [S] para sim
    tecle [N] para não
    """)
    opcao = input(": ")
    system("cls")
    if opcao in ["s","S","n","N"]:
        if opcao in ["s","S"]:
            print("Obrigado por Usar")
            sair = True
            return sair
        else:
            print("comando inválido. Tente novamente")
            input("\nPressione ENTER para continuar")
    else:
        print("comando inválido. Tente novamente")
        input("\nPressione ENTER para continuar")

while True:
    opcaoEscolhida = menuDeopções()
    comando = RodarOpçãoDoMenu(opcaoEscolhida)
    if comando:
        break