from flask import *
from bancoDeDados.mainDB import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulacao')
def simulacao():
    return render_template('simulacao.html')

@app.route('/ongrid')
def ongrid():
    return render_template('ongrid.html')

@app.route('/offgrid')
def offgrid():
    return render_template('offgrid.html')

@app.route('/hybrid', methods=("GET", "POST"))
def hybrid():

    if request.method == "GET":
        return render_template('hybrid.html')

    if request.method == "POST":

        resultado = conexao.manipularBanco(f'''
            INSERT INTO "hybrid"
            values(DEFAULT , DEFAULT , '{request.form['KWHRDIA']}', '{request.form['ENERGIASOL']}', '{request.form['ESTADO']}', '{request.form['CIDADE']}', '{request.form['BATERIAVOLTS']}', '{request.form['ENERGIADIARESERVA']}', '{request.form['PAINELTIPO']}', '{request.form['MODULOWATT']}', '{request.form['TEMPERATURAOPCAO']}', '{request.form['PERDASINVERSOR']}', '{request.form['FATORSEGURANCAINVERSOR']}', '{request.form['PERDASCABO']}', '{request.form['PERDASINCOMPATIBILIDADE']}', '{request.form['PERDASSUJEIRA']}', '{request.form['PROFUNDIDADE']}', '{request.form['BATERIAEFICIENCIA']}')
            ''')
        
        if resultado:

            return redirect(url_for("home"))
        else:
            return "Erro na inserção"

@app.route('/login', methods=("GET", "POST"))
def login():
    if request.method == "GET":
        return render_template('login.html')
    
    if request.method == "POST":

        resultado = conexao.manipularBanco(f'''
            INSERT INTO "endereco"
            values( DEFAULT ,'CEP','UF', 'CIDADE', 'BAIRRO', 'NOME', 'COMPLEMENTO' , DEFAULT)
            ''')
        
        if resultado:

            return redirect(url_for("home"))
        else:
            return "Erro na inserção"

if __name__ == "__main__":
    app.run(debug=True)
