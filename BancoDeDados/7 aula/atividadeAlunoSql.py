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


try:
    conn = psycopg2.connect(
    dbname = "Escola", host = "localhost",
    port="5432", user="postgres", 
    password="postgres"
    ) # mudar o dbname quando colocar para rodar na aula
    cursor = conn.cursor()
    print("Conectado com sucesso")
    criarTabelas()
    print("Tabelas criadas com sucesso")
    conn.commit()
    cursor.close()
    conn.close()

except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro!",error)
print()

