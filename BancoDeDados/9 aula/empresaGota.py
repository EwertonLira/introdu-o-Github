import psycopg2
# pega informações do banco de dados empresa

#------------
# tabela já criadas.
def criarEntidadeFuncionário():
    sql = '''
    CREATE TABLE "Funcionário" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" VARCHAR(255) NOT NULL,
    "Cpf" CHAR(11) NOT NULL,
    "Salário" MONEY NOT NULL DEFAULT 0,
    "Cargo" VARCHAR(255) NOT NULL DEFAULT 'autônomo',
    "IdDepartamento" INT NOT NULL DEFAULT 1,
    CONSTRAINT fk_departamento
        FOREIGN KEY ("IdDepartamento")
        REFERENCES "Departamento"("Id")
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
    );
    '''
    return sql

def criarEntidadeDepartamento():
    sql = '''
    CREATE TABLE "Departamento" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" VARCHAR(255) NOT NULL
    );
    '''
    return sql
# ---------------

def verFuncionarioEspecifico(id):

    cursor.execute(f'''
    Select * from "Funcionário"
    WHERE "Id" = '{id}'
    ''')    

    funcionario = cursor.fetchone()

    if funcionario:
        print(f'''
        ID: {funcionario[0]}
        Nome: {funcionario[1]}
        CPF : {funcionario[2]}
        Salário: R$ {funcionario[3]}
        Cargo: {funcionario[4]}
        Departamento: {funcionario[5]}
        ''')

    else:
        print("Funcionário não encontrado.")

def verDepartamentoEspecifico(id):

    cursor.execute(f'''
    Select * from "Departamento"
    WHERE "Id" = '{id}'
    ''')

    departamento = cursor.fetchone()

    if departamento:
        print(f'''
        ID: {departamento[0]}
        Nome: {departamento[1]}
        ''')

    else:
        print("Departamento não encontrado.")

def verFuncionarios():

    cursor.execute('''
                SELECT * FROM "Funcionário"
                ORDER BY "Id" ASC
                ''')

    listaFuncionarios = cursor.fetchall()
    print("ID - Nome")
    for funcionario in listaFuncionarios:
        print(f"{funcionario[0]} - {funcionario[1]}")

    idEscolhido = input(f'''
Digite o id de um funcionário que deseja ver mais informações
: ''')

    try:
        int(idEscolhido)
        if idEscolhido != "0" or " " or "sair":
            verFuncionarioEspecifico(idEscolhido)
        else:
            print("Voltando para o menu principal.")
    except:
        print("comando inválido")

def verDepartamentos():

    cursor.execute('''
                SELECT * FROM "Departamento"
                ORDER BY "Id" ASC
                ''')

    listaDepartamentos = cursor.fetchall()
    print("ID - Nome")
    for departamento in listaDepartamentos:
        print(f"{departamento[0]} - {departamento[1]}")

    idEscolhido = input(f'''
escolha o id do departamento para ver mais detalhes.
: ''')

    if idEscolhido != "0":
        verDepartamentoEspecifico(idEscolhido)
    else:
        print("Voltando para o menu principal.")

def inserirFuncionario():
    print("Você está cadastrando um funcionário.")

    novoFuncionarioNome = input("Digite o nome do novo funcionário: ")
    novoFuncionarioCpf = input("Digite o CPF do funcionário: ")
    novoFuncionarioSalario = input("Digite o salário do novo funcionário: ")
    novoFuncionarioCargo = input("Digite o cargo do novo funcionário: ")
    novoFuncionarioIdDepartamento = input("Digite o departamento do novo funcionário: ")

    cursor.execute(f'''
    INSERT INTO "Funcionário"
    Values(default, '{novoFuncionarioNome}', '{novoFuncionarioCpf}' , '{novoFuncionarioSalario}', '{novoFuncionarioCargo}', '{novoFuncionarioIdDepartamento}')
    
    ''')

    conn.commit()

    print("Funcionário Inserido!")

def inserirDepartamento():
    print("Você está cadastrando um departamento.")

    novoDepartamentoNome = input("Digite o nome do novo departamento: ")


    cursor.execute(f'''
    INSERT INTO "Departamento"
    Values(default, '{novoDepartamentoNome}')
    
    ''')

    conn.commit()

    print("Departamento Inserido!")

def deletarFuncionarios():
    print("escolha o funcionário que deseja excluir")
    cursor.execute('''
                SELECT * FROM "Funcionário"
                ORDER BY "Id" ASC
                ''')

    listaFuncionarios = cursor.fetchall()
    print("ID - Nome")
    for funcionario in listaFuncionarios:
        print(f"{funcionario[0]} - {funcionario[1]}")

    opcao = input(": ")
    
    cursor.execute(f'''
    DELETE FROM
        Funcionário
        WHERE
        id = '{opcao}'    
    ''')

def pesquisarFuncionario():

    pass

def opçãoSair():
    print("Saindo do programa...")
    cursor.close()
    conn.close()

def menu():
    # menu da aplicação

    while True:
        print('''
        👨‍💼👨‍💼 Empresa gota 👨‍💼👨‍💼

escolha uma das opções abaixo digitando
a letra correspondente e aperte [ENTER]
        
    [A] - ver funcionários
    [S] - ver departamentos
    [D] - Inserir departamento
    [F] - Inserir funcionário
    [E] - Excluir funcionário
    [Q] - Pesquisar funcionário
    [Z] - sair
        ''')
        op = input(": ")

        match op:
            case "a" | "A":
                verFuncionarios()
            case "s" | "S":
                verDepartamentos()
            case "d" | "D":
                inserirDepartamento()
            case "f" | "F":
                inserirFuncionario()
            case "e" | "E":
                deletarFuncionarios()
            case "q" | "Q":
                pesquisarFuncionario()
            case "z" | "Z":
                opçãoSair()
                break
            case _:
                print("Opção inválida. Digite novamente!")

        input("Tecle enter para continuar.")

# -------------início do programa-------------

try:
    conn = psycopg2.connect(dbname="empresaGota", host="localhost",port="5432",user="postgres",password="postgre")
    cursor = conn.cursor()

    # cursor.execute(criarEntidadeDepartamento())
    # conn.commit()

    # cursor.execute(criarEntidadeFuncionário())
    # conn.commit()

    # print("tabelas criadas.")

    # cursor.close()
    # conn.close()

    menu()

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro ao tentar a conexão", error)


    