
caminho = "listaRevisaoArmazenandoDados/5 atividade/conta.txt"

class Conta():
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo

    def getTitular(self):
        return self._titular

    def getSaldo(self):
        return self._saldo
    
def maiorConta(listaObjConta):
    aux = 0
    for cadaObjConta in listaObjConta:
        if cadaObjConta.getSaldo() > aux:
            objSalvo = cadaObjConta
            aux = cadaObjConta.getSaldo()
    
    return objSalvo

def salvarTxt(valorParaTxt):
    with open(caminho, "w",newline="") as fileTxt:
        fileTxt.write(valorParaTxt)

def abrirTxt():
    with open(caminho) as fileTxt:
        contaTxtLidos = fileTxt.read()
    
    return contaTxtLidos

carla = Conta("Carla",300)
joão = Conta("João",100)
miguel = Conta("Miguel",950)
andre = Conta("Andre", 600)
rafael = Conta("Rafael",900)

# vai retornar a maior conta como um objeto
listaDeContas = [carla,joão,andre,miguel,rafael]
objResutado = maiorConta(listaDeContas)

# com o objeto com o maior saldo. pegamos o saldo do objeto e convertemos para texto
valorTexto = objResutado.getSaldo()
valorTexto = str(valorTexto)

# salvamos o texto no arquivo txt
salvarTxt(valorTexto)

# abrimos o arquivo de texto Txt
valorAbertoTxt = abrirTxt()

# printamos o nome do objeto e o valor guardado no arquivo txt.
print(f"O maior saldo é de {objResutado.getTitular()} com o valor de R$ {valorAbertoTxt}")