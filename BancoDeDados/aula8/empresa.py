import psycopg2
# pega informações do banco de dados empresa

#------------
# tabela já criadas.
def criarEntidadeFuncionário():
    sql = '''
    CREATE TABLE "Funcionário" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" VARCHAR(255) NOT NULL,
    "Salário" MONEY NOT NULL DEFAULT 0,
    "Cargo" VARCHAR(255) NOT NULL DEFAULT 'autônomo',
    "IdDepartamento" INT NOT NULL DEFAULT 1
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
        Salário: R$ {funcionario[2]}
        Cargo: R$ {funcionario[3]}
        Departamento: {funcionario[4]}
        ''')

    else:
        print("Funcionário não encontrado.")

def verDepartamentoEspecifico(id):

    cursor.execute(f'''
    Select * from "Departamentos"
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

def verFuncionarios(cursor):

    cursor.execute('''
                SELECT * FROM "Funcionário"
                ORDER BY "Id" ASC
                ''')

    listaFuncionarios = cursor.fetchall()
    print("ID - Nome")
    for funcionario in listaFuncionarios:
        print(f"{funcionario[0]} - {funcionario[1]}")

    idEscolhido = input("Digite o id de um funcionário que deseja ver mais informações:(0 = Voltar) ")

    if idEscolhido != "0":
        verFuncionarioEspecifico(idEscolhido)
    else:
        print("Voltando para o menu principal.")

def verDepartamentos():

    cursor.execute('''
                SELECT * FROM "Departamentos"
                ORDER BY "Id" ASC
                ''')

    listaDepartamentos = cursor.fetchall()
    print("ID - Nome")
    for departamento in listaDepartamentos:
        print(f"{departamento[0]} - {departamento[1]}")

    idEscolhido = input("Digite o id de um departamento que deseja ver mais informações:(0 = Voltar) ")

    if idEscolhido != "0":
        verDepartamentoEspecifico(idEscolhido)
    else:
        print("Voltando para o menu principal.")

def inserirFuncionario():
    print("Você está cadastrando um funcionário.")

    novoFuncionarioNome = input("Digite o nome do novo funcionário: ")
    novoFuncionarioSalario = input("Digite o salário do novo funcionário: ")
    novoFuncionarioCargo = input("Digite o cargo do novo funcionário: ")
    novoFuncionarioIdDepartamento = input("Digite o departamento do novo funcionário: ")

    cursor.execute(f'''
    INSERT INTO "Funcionário"
    Values(default, '{novoFuncionarioNome}', '{novoFuncionarioSalario}', '{novoFuncionarioCargo}', '{novoFuncionarioIdDepartamento}')
    
    ''')

    conn.commit()

    print("Funcionário Inserido!")

def inserirDepartamento():
    print("Você está cadastrando um departamento.")

    novoDepartamentoNome = input("Digite o nome do novo departamento: ")


    cursor.execute(f'''
    INSERT INTO "Departamentos"
    Values(default, '{novoDepartamentoNome}')
    
    ''')

    conn.commit()

    print("Departamento Inserido!")

def deletarFuncionarios():
    cursor.execute(f'''
    
    
    ''')

def opçãoSair():
    print("Saindo do programa...")
    cursor.close()
    conn.close()

def menu(cursor,conn):
    # menu da aplicação

    while True:
        print('''
        👨‍💼 Empresa soluções xyz 📈

escolha uma das opções abaixo digitando
a letra correspondente e aperte [ENTER]
        
    [a] - ver funcionários
    [s] - ver departamentos
    [d] - Inserir departamento
    [f] - Inserir funcionário
    [z] - sair
        ''')
        op = input(": ")

        match op:
            case "a" | "A":
                verFuncionarios(cursor)
            case "s" | "S":
                verDepartamentos()
            case "d" | "D":
                inserirDepartamento()
            case "f" | "F":
                inserirFuncionario()
            case "e" | "E":
                pass
            case "z" | "Z":
                opçãoSair()
                break
            case _:
                print("Opção inválida. Digite novamente!")

        input("Tecle enter para continuar.")

try:
    conn = psycopg2.connect(dbname="Empresa xyz", host="localhost",port="5432",user="postgres",password="postgre")
    cursor = conn.cursor()

    # cursor.execute(criarEntidadeFuncionário()) # tabela do banco de dados já criada
    # conn.commit()

    # cursor.execute(criarEntidadeDepartamento()) # tabela no banco de dados já criada
    # conn.commit()

    # print("tabelas criadas.")

    # cursor.close()
    # conn.close()

    menu(cursor,conn)

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro ao tentar a conexão", error)


    