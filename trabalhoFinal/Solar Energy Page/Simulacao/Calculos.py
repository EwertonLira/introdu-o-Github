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