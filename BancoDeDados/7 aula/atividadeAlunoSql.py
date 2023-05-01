import psycopg2

def criarTabelas():

    cursor.execute('''
    CREATE TABLE "Alunos" (
    "nroMatricula" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "nome" varchar(255) NOT NULL,
    "cpf" char(11),
    "endereço" varchar(255) default 'não informado',
    "telefone" char(11),
    "anoNascimento" char(4)
    );
    ''')

    cursor.execute('''
    Create Table "Disciplina" (
    "codDisciplina" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "nomne" varchar(255) NOT NULL,
    "codigo_do_curso" varchar(3) NOT NULL
    );
    ''')

    cursor.execute('''
    Create Table "Matrícula" (
    "idMatrícula" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "nroMatrícula" int NOT NULL,
    "codDisciplina" int NOT NULL,
    "sementre" varchar(2) NOT NULL,
    "ano" char(4) NOT NULL,
    "nota" numeric(3,2),
    "nroFaltas" int
    );
    ''')

def adicionarColunasTabelas():
    # comando para modificar tabelas já criadas
    cursor.execute('''
    ALTER TABLE "Alunos"
    ADD COLUMN "Idade" VARCHAR(3);
    ''')

def DropTable():
    # comando para apagar completamente uma tabela, ela não limpa os dados dos campos da tabela,
    cursor.execute('''
    DROP TABLE "ArquivoMorto";
    ''')

def verAluno():

    cursor.execute('''
    SELECT * FROM "Alunos"
    ORDER BY "nroMatricula" ASC
    ''')

    listaAluno = cursor.fetchall()
    print("Matrícula - Nome")
    verificarId = []
    for aluno in listaAluno:
        print(f"{aluno[0]} - {aluno[1]}")
        verificarId.append(str(aluno[0]))

    print("Digite a matrícula de um Aluno que deseja ver mais informações:\n(aperte qualquer tecla para voltar) ")
    idEscolhido = input(": ")

    if idEscolhido in verificarId:
        verAlunoEspecifico(idEscolhido)
        verificarId.clear()
    
def inserirAluno():
    
    print("Você está cadastrando um Aluno.")

    novoAlunoNome = input("Digite o nome do novo Aluno: ")
    novoAlunoCpf = input("Digite o CPF do novo Aluno: ")
    novoAlunoEndereco = input("Digite o Endereço do novo Aluno: ")
    novoAlunoTelefone = input("Digite o Telefone do novo Aluno: ")
    novoAlunoNascimento = input("Digite o Ano de Nascimento do novo Aluno: ")

    cursor.execute(f'''
    INSERT INTO "Alunos"
    Values(default, '{novoAlunoNome}', '{novoAlunoCpf}', '{novoAlunoEndereco}', '{novoAlunoTelefone}', '{novoAlunoNascimento}')
    ''')

    conn.commit()

    print("Aluno Inserido!")

def verAlunoEspecifico(id):

    cursor.execute(f'''
    Select * from "Alunos"
    WHERE "nroMatricula" = '{id}'
    ''')

    aluno = cursor.fetchone()

    if aluno:
        print(f'''
        Matrícula: {aluno[0]}
        Nome: {aluno[1]}
        CPF: {aluno[2]}
        Endereço: {aluno[3]}
        Telefone: {aluno[4]}
        Ano de nascimento: {aluno[5]}
        ''')

    else:
        print("Aluno não encontrado.")

def AtualizarAluno():
    print("Selecione um aluno para atualizar da lista abaixo")
    
    cursor.execute('''
    SELECT * FROM "Alunos"
    ORDER BY "nroMatricula" ASC
    ''')

    listaAluno = cursor.fetchall()
    print("matrícula - Nome")
    verificarId = []
    for aluno in listaAluno:
        print(f"{aluno[0]} - {aluno[1]}")
        verificarId.append(str(aluno[0]))

    idEscolhido = input("Digite número da matrícula de um Aluno que deseja Alterar: ")
    
    if idEscolhido in verificarId:
        verificarId.clear()
        nome,cpf,endereço,telefone,nascimento,todos = "Nome","CPF", "Endereço","Telefone","Ano de nascimento","Todos"
        print(f"""em qual campo deseja fazer a alteração:
[1] {nome}
[2] {cpf}
[3] {endereço}
[4] {telefone}
[5] {nascimento}
[6] {todos}
[0] Cancelar
    """)
        op = input(": ")
        match op:
            case "1":
                opTexto = nome
                opCase = "nome"
            case "2":
                opTexto = cpf
                opCase = "cpf"
            case "3":
                opTexto = endereço
                opCase = "endereço"
            case "4":
                opTexto = telefone
                opCase = "telefone"
            case "5":
                opTexto = nascimento
                opCase = "anoNascimento"
            
            case "6":
                valorNome = input("Insira o novo nome do Aluno: ")
                valorCpf = input("Insira o novo CPF do Aluno: ")
                valorEndereco = input("Insira o novo Endereço do Aluno: ")
                valorTelefone = input("Insira o novo Telefone do Aluno: ")
                valorNascimento = input("Insira o novo Ano de nascimento do Aluno: ")

                cursor.execute(f'''UPDATE "Alunos"
            SET "nome" = '{valorNome}',
                "cpf" = '{valorCpf}',
                "endereço" = '{valorEndereco}',
                "telefone" = '{valorTelefone}',
                "anoNascimento" = '{valorNascimento}'        
            WHERE "nroMatricula" = '{idEscolhido}';  
            ''')
                conn.commit()
                print("Atualização feita com sucesso")
            
            case "0":
                print("voltando ao menu principal")
            case _:
                print("Comando Inválido")
        
        acesso = ["1","2","3","4","5"]
        if op in acesso:
            print(f"Insira o novo {opTexto} do Aluno")
            novoValor = input(": ")

            cursor.execute(f'''UPDATE "Alunos"
            SET "{opCase}" = '{novoValor}'
            WHERE "nroMatricula" = '{idEscolhido}';  
            ''')
            conn.commit()
            print("Atualização feita com sucesso")

    else:
        print("Voltando para o menu principal.")

def DeletarAluno():
    print("escolha o aluno que deseja excluir")
    cursor.execute('''
                SELECT * FROM "Alunos"
                ORDER BY "nroMatricula" ASC
                ''')

    listaAlunos = cursor.fetchall()
    print("Matrícula - Nome")
    VerificarID = []
    for aluno in listaAlunos:
        print(f"{aluno[0]} - {aluno[1]}")
        VerificarID.append(aluno[0])

    opcao = input(": ")
    if int(opcao) in VerificarID:
        cursor.execute(f'''
        DELETE 
            FROM "Alunos"
            WHERE
            "nroMatricula" = '{opcao}' 
        ''')
        print("aluno removido com sucesso!")
        conn.commit()
    else:
        print("comando inválido")
   
def opçãoSair():
    print("Saindo do programa...")
    cursor.close()
    conn.close()

def menu():
    # menu da aplicação

    while True:
        print('''
        👨‍💼 Escola 📈

escolha uma das opções abaixo digitando
a letra correspondente e aperte [ENTER]
        
    [a] - Ver Aluno
    [s] - Inserir novo Aluno
    [d] - Atualizar Aluno
    [f] - Deletar Aluno
    [z] - sair
        ''')
        op = input(": ")

        match op:
            case "a" | "A":
                verAluno()
            case "s" | "S":
                inserirAluno()
            case "d" | "D":
                AtualizarAluno()
            case "f" | "F":
                DeletarAluno()
            case "z" | "Z":
                opçãoSair()
                break
            case _:
                print("Opção inválida. Digite novamente!")

        input("Tecle enter para continuar.")

try:
    conn = psycopg2.connect(
    dbname = "Escola", host = "localhost",
    port="5432", user="postgres", 
    password="postgres"
    ) # mudar o dbname quando colocar para rodar na aula
    cursor = conn.cursor()
    print("Conectado com sucesso")
    # criarTabelas() tabelas já criadas
    # print("Tabelas criadas com sucesso")
    # conn.commit()
    # cursor.close()
    # conn.close()
    menu()

except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro!",error)

