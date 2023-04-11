import csv
caminho = "listaRevisaoArmazenandoDados/4 atividade/aluno.csv"

class Aluno:
    def __init__(self,nome, matrícula, notas):
        self._nome = nome
        self._matrícula = matrícula
        self._notas = notas
    
    def getNome(self):
        return self._nome
    
    def getMatrícula(self):
       return self._matrícula
    
    def getNotas(self):
       return self._notas

def calcularMédia(objaluno):
    #notas = objaluno.getNotas()
    
    médiaAluno = sum(objaluno.getNotas()) / (len(objaluno.getNotas()))
    return médiaAluno

def SalvarCSV(objAluno,médiaAluno):
    with open(caminho, "w", newline = "" ) as alunoCsv:
        EscreverNoCsv = csv.writer(alunoCsv)

        EscreverNoCsv.writerow(["nome","matrícula","notas","média"])
    
        nome = objAluno.getNome()
        matrícula = objAluno.getMatrícula()
        notas = objAluno.getNotas()
        
        EscreverNoCsv.writerow([nome,matrícula,notas,médiaAluno])
    
def abrirMédiaArquivoCSV():
    # abrir o arquivo e tirar somente a média
    
    with open(caminho, "r") as arquivoCSV:
        arquivoCsvLido = csv.reader(arquivoCSV, delimiter=",")
        for cadaListaCsv in arquivoCsvLido:
            
            if cadaListaCsv[3] == "média":
                continue

            mediaAluno = cadaListaCsv[3]
            nome = cadaListaCsv[0]
        
        return nome , mediaAluno  

# notas em formato de lista
notasPaulo = [10,10,9.5,10]

# classe istanciada
Paulo = Aluno("Paulo","1234",notasPaulo)

# a média é criada com o objeto Paulo
médiaPaulo = calcularMédia(Paulo)

# é salvo os dados do aluno e a sua média
SalvarCSV(Paulo,médiaPaulo)

# retornar o nome do Aluno e a sua média do csv
nomeCsv , médiaCSv = abrirMédiaArquivoCSV()
print(f"a média de {nomeCsv} foi de {(float(médiaCSv)):.2f}")