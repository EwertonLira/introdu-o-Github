# Criar um site com 2 opções: Ver Pokemons e Inserir Pokemons

# Na página Ver Pokemons você deve mostrar uma lista de pokemons, de um banco de dados

# Na página Inserir Pokemons você deve criar um formulário e inserir o pokemon no banco de dados.



from flask import *
from control.classConexao import Conexao

con = Conexao("pokemon","localhost","5432","postgres","postgre")

app = Flask(__name__)
@app.route('/pokedex')
def home():
    
    pokemons = con.consultarBanco("""
    select * from "Pokedex"
    """)
    return render_template("/pokedex", pokemons = pokemons)

@app.route('/saida')
def saida():
    return "tchau word"

if __name__=="__main__":
    app.run(debug=True,port=5050)