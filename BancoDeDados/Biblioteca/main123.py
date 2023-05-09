from control.SQlexecutar import *
from model.classLivro import *

caminho = "model\comandos.sql"
comandoSQL = "selectID"

resultado = executarSQL(livroTeste,caminho,"selectID","1")