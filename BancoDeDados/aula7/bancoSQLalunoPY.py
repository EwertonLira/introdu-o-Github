import psycopg2

try:
    conn = psycopg2.connect(
    dbname = "Escola 2", host = "localhost",
    port="5432", user="postgre", 
    password="postgres"
    )
    cursor = conn.cursor()
    print("Conectado com sucesso")

    cursor.execute('''
    CREATE TABLE "Alunos" (
    "NroMatricula" serial,
    "Nome" varchar(255) NOT NULL,
    "CPF" char(11) NOT NULL,
    "Endereço" varchar(255) default 'não informado',
    "Telefone" char(11)


    )
    
    
    ''')


except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro!",error)
print()