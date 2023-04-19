import psycopg2 # pip install psycopg2

conn = psycopg2.connect(dbname = "Escola", host = "localhost", port="5432", user="postgres", password="postgres") #Porta padrão 5432

cursor = conn.cursor()

cursor.execute('''

SELECT * FROM "alunos"
ORDER BY "NroMatrícula" ASC

''')

print(cursor.description) # para ver as colunas use o cursor.description

# for aluno in cursor.fetchall():
#     print(f"{aluno[0]} - {aluno[2]}")

for aluno in cursor.fetchall():
    print(f'''
    {aluno[0]},"==",{type(aluno[0])}
    {aluno[1]},"==",{type(aluno[1])}
    {aluno[2]},"==",{type(aluno[2])}
    {aluno[3]},"==",{type(aluno[3])}
    {aluno[4]},"==",{type(aluno[4])}
    {aluno[5]},"==",{type(aluno[5])}
    ''')


cursor.execute('''
SELECT table_name FROM information_schema.tables -- código SQL para retornar as tabelas disponíveis
    WHERE table_schema = 'public'
''')

print(cursor.fetchall())

conn.close()
