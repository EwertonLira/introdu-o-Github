import psycopg2

conn = psycopg2.connect(
dbname = "alunos", host = "localhost",
port="5432", user="postgres", 
password="postgre"
)

cursor = conn.cursor()

cursor. execute('''
SELECT * FROM "Alunos"
''')

print(cursor.fetchall())