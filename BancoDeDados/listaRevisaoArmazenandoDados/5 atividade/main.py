
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
joão = Conta("João",700)
miguel = Conta("Miguel",950)
andre = Conta("Andre", 600)
rafael = Conta("Rafael",900)

listaDeContas = [carla,joão,andre,miguel,rafael]
salvarTxt(listaDeContas)
valorAbertoTxt = abrirTxt()
print(valorAbertoTxt)
objResutado = maiorConta(listaDeContas)
print(f"O maior saldo é de {objResutado.getTitular()} com o valor de R$ {objResutado.getSaldo()}")