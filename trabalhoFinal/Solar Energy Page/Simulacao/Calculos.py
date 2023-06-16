import csv

# ////////////////////// variáveis///////
mediaAnual = ""
radiacao = ""
eficienciaSistema90 =""

placaAdotada = ""

numeroDePlacas = ""

def capacidadeDoSistema():
    resultado = mediaAnual/365/radiacao/eficienciaSistema90

    return resultado

def numeroDePlacas():
    resultado = capacidadeDoSistema()/ placaAdotada
    return resultado

def preco():
    resultado = placaAdotada * numeroDePlacas
    return resultado


caminho = "Simulacao\dados_calculo.csv"
def abrirCsv():

    with open(caminho, "r") as arquivo:
        arquivoCsv = csv.reader(arquivo, delimiter=";")
        for linha in arquivoCsv:
            print(linha)
        # for i, linha in enumerate(arquivoCsv):
        #     if i == 0:
        #         print("cabeçalho: "+str(linha))
        #     else:
        #         print("valor: "+str(linha))
    
abrirCsv()