
from flask import *
from Controle.classConexao import Conexao
import env

Conexao

app = Flask(__name__)
conexaoBanco = Conexao(env.databaseName, env.hostName, env.port, env.userName, env.password)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokemons")
def verPokemons():
    pass

if __name__=="__main__":

    app.run(debug=True, port=5050)