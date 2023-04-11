caminho = "listaRevisaoArmazenandoDados/3 atividade/area.txt"

class Retângulo():
    def __init__(self,altura,largura):
        self._altura = altura
        self._largura = largura

    def getAltura(self):
        return self._altura
    
    def getLargura(self):
        return self._largura
    
def calcularArearetângulo(objRetângulo):
    area = objRetângulo.getAltura() * objRetângulo.getLargura()
    return area

def escreverAreaTxt(valorDaArea):
    valorDaArea = str(valorDaArea)

    with open(caminho,"w") as areaTxt:
        areaTxt.write(valorDaArea)
    
def lerAreaTxt():
    with open(caminho) as areaTxt:
        valorAreaStr = areaTxt.read()
    
    valorArea = int(valorAreaStr)

    return valorArea

# classe istânciada
quatroCantos = Retângulo(10,20)

# objeto é colocado dentro da função para retornar o resultado da área
resultadoArea = calcularArearetângulo(quatroCantos)

# resultado é salvo no arquivo txt
escreverAreaTxt(resultadoArea)

# retornar o conteúdo do arquivo txt
dadoDoTxt = lerAreaTxt()

print("o valor da área é:",dadoDoTxt)
