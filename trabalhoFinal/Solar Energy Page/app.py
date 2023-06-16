from flask import *
from bancoDeDados.mainDB import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulacao')
def simulacao():
    return render_template('simulacao.html')

@app.route('/ongrid', methods=("GET", "POST"))
def ongrid():
    if request.method == "GET":
        return render_template('ongrid.html')

    if request.method == "POST":

        resultado = conexao.manipularBanco(f'''
            INSERT INTO "sistema"
            values(DEFAULT , DEFAULT , 'ONGRID', '{request.form['KWHRDIA']}', '{request.form['ENERGIASOL']}', '{request.form['ESTADO']}', '{request.form['CIDADE']}', 'NÃO UTILIZA BATERIAVOLTS', 'NÃO UTILIZA ENERGIADIARESERVA', '{request.form['PAINELTIPO']}', '{request.form['MODULOWATT']}', '{request.form['TEMPERATURAOPCAO']}', '{request.form['PERDASINVERSOR']}', '{request.form['FATORSEGURANCAINVERSOR']}', '{request.form['PERDASCABO']}', '{request.form['PERDASINCOMPATIBILIDADE']}', '{request.form['PERDASSUJEIRA']}', 'NÃO UTILIZA PROFUNDIDADE', 'NÃO UTILIZA BATERIAEFICIENCIA' )
            ''')
        
        if resultado:

            return redirect(url_for("login"))
        else:
            return "Erro na inserção"


@app.route('/offgrid', methods=("GET", "POST"))
def offgrid():
    if request.method == "GET":
        return render_template('offgrid.html')

    if request.method == "POST":

        resultado = conexao.manipularBanco(f'''
            INSERT INTO "sistema"
            values(DEFAULT , DEFAULT , 'OFFGRID', '{request.form['KWHRDIA']}', 'NÃO UTILIZA ENERGIASOL', '{request.form['ESTADO']}', '{request.form['CIDADE']}', '{request.form['BATERIAVOLTS']}', '{request.form['ENERGIADIARESERVA']}', '{request.form['PAINELTIPO']}', '{request.form['MODULOWATT']}', '{request.form['TEMPERATURAOPCAO']}', '{request.form['PERDASINVERSOR']}', '{request.form['FATORSEGURANCAINVERSOR']}', '{request.form['PERDASCABO']}', '{request.form['PERDASINCOMPATIBILIDADE']}', '{request.form['PERDASSUJEIRA']}', '{request.form['PROFUNDIDADE']}', '{request.form['BATERIAEFICIENCIA']}')
            ''')
        
        if resultado:

            return redirect(url_for("login"))
        else:
            return "Erro na inserção"

@app.route('/hybrid', methods=("GET", "POST"))
def hybrid():

    if request.method == "GET":
        return render_template('hybrid.html')

    if request.method == "POST":

        resultado = conexao.manipularBanco(f'''
            INSERT INTO "sistema"
            values(DEFAULT , DEFAULT , 'HYBRID', '{request.form['KWHRDIA']}', '{request.form['ENERGIASOL']}', '{request.form['ESTADO']}', '{request.form['CIDADE']}', '{request.form['BATERIAVOLTS']}', '{request.form['ENERGIADIARESERVA']}', '{request.form['PAINELTIPO']}', '{request.form['MODULOWATT']}', '{request.form['TEMPERATURAOPCAO']}', '{request.form['PERDASINVERSOR']}', '{request.form['FATORSEGURANCAINVERSOR']}', '{request.form['PERDASCABO']}', '{request.form['PERDASINCOMPATIBILIDADE']}', '{request.form['PERDASSUJEIRA']}', '{request.form['PROFUNDIDADE']}', '{request.form['BATERIAEFICIENCIA']}')
            ''')
        
        if resultado:

            return redirect(url_for("login"))
        else:
            return "Erro na inserção"

# Rota principal - página de login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "GET":
        return render_template('login.html')
    
    if request.method == "POST":
        # nome = request.form["nome"]
        # sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form["senha"]
        
        # conn = connect_to_db()
        # cur = conn.cursor()
        # cur.execute("SELECT * FROM users WHERE nome = %s AND sobrenome = %s AND email = %s AND senha = %s", (nome, sobrenome, email, senha))
        # //////////fazer um select para conferir os dados.
        resultado = conexao.consultarBanco(f'''SELECT "registro_email","registro_senha" FROM "registro" WHERE "registro_email" = '{email}' ;''')
        user = False
        if resultado:
            resultado = resultado[0] # tirar da primeira lista os resultados
            emailDB = resultado[0]
            senhaDB = resultado[1]
            print("email",emailDB,"senha",senhaDB)
            print(email,senha)
            if email == emailDB and senha == senhaDB:
                user = True

        # user = cur.fetchone()
        # cur.close()
        # conn.close()

        if user:
            # session["nome"] = user[1]  # Armazena o nome de usuário na sessão
            return redirect("/address")
        else:
            return render_template('login.html', error="Credenciais inválidas. Tente novamente.")

    return render_template('login.html')

# Rota para o registro de um novo usuário
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form["senha"]

        # conn = connect_to_db()
        # cur = conn.cursor()
        # cur.execute("INSERT INTO users (nome, sobrenome, email, senha) VALUES (%s, %s, %s, %s)", (nome, sobrenome, email, senha))
        resultado = conexao.manipularBanco(f'''
            INSERT INTO "registro"
            values(DEFAULT , DEFAULT , '{nome}', '{sobrenome}', '{email}', '{senha}')
            ''')
        # conn.commit()
        # cur.close()
        # conn.close()

        return redirect('/login')
    
    return render_template("register.html")

@app.route('/address', methods=("GET", "POST"))
def address():
    if request.method == "GET":
        return render_template('address.html')
    
    if request.method == "POST":

        resultado = conexao.manipularBanco(f'''
            INSERT INTO "endereco"
            values( DEFAULT , DEFAULT ,'{request.form['CEP']}','{request.form['RUA']}', '{request.form['NUMERO']}', '{request.form['COMPLEMENTO']}', '{request.form['BAIRRO']}', '{request.form['CIDADE']}', '{request.form['ESTADO']}')
            ''')
        
        if resultado:

            return redirect(url_for("pay"))
        else:
            return "Erro na inserção"

# Rota para fazer logout
@app.route("/logout")
def logout():
    session.pop("nome", None)
    return redirect("/login")

@app.route('/pay', methods=("GET", "POST"))
def pay():

    if request.method == "GET":
        return render_template('pay.html')

    if request.method == "POST":
        resultado = conexao.manipularBanco(f'''
            INSERT INTO "cartao"
            values( DEFAULT , DEFAULT ,'{request.form['NUMERO']}','{request.form['TITULAR']}', '{request.form['MES']}', '{request.form['ANO']}', '{request.form['CVV']}')
            ''')
        
        if resultado:

            return redirect(url_for("home"))
        else:
            return "Erro na inserção"

if __name__ == "__main__":
    app.run(debug=True)
