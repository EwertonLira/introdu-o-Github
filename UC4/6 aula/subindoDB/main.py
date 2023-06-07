# site dashboard.render.com
# PSQL Command tem o link url do hostname(fazemos isso porque estamos usando o psycopg2)
# mudar o nome do dono do banco que gerou o arquivo e colocar o nome do usuario do banco render

# função^: um banco com linguagem postgreSql online por 90 dias.

from Controle.classConexao import Conexao
import dotenv
import os
from pokemonNovo import sqlbackup
dotenv.load_dotenv()

####### conexão criada do banco de dados
conexaoBanco = Conexao(os.getenv("DBNAMEDB"), os.getenv("HOSTDB"), os.getenv("PORTDB"), os.getenv("USERNAMEDB"), os.getenv("PASSWORDDB"))

######## inserir o backup no banco de dados
#conexaoBanco.manipularBanco(sqlbackup)

###### modo para ler o arquivo
#caminho = "C:\Users\aluno turma 2\Documents\Ewerton Lira\python\pastaGithubPython\introdu-o-Github\UC4\6 aula\subindoDB\pokemonNovo.py"
# print(conexaoBanco.manipularBanco(open( caminho, "r").read()))


pokedex = conexaoBanco.consultarBanco('''SELECT * FROM "Pokedex"''')
for pokemon in pokedex:
    print(pokemon[0], end=" ")
    print(pokemon[1], end=" ")
    print(pokemon[2], end=" ")
    print(pokemon[3], end=" ")
    print(pokemon[4], end=" ")
    print(pokemon[5])



