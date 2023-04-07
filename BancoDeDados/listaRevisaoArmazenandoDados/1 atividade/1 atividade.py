import csv
caminho = "listaRevisaoArmazenandoDados/1 atividade/pessoas.csv"

class Pessoa:
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade

    def getNome(self):
        return self._nome

    def getIdade(self):
        return self._idade

def levarObjetoParaCSV(ListaObjeto):
    # Usar a lista de objetos para a função que vai converter os dados para o arquivo csv
       
    with open(caminho, 'w', newline='') as csvfile: #newline faz as linhas ficarem um abaixo da outra sem espaço
        escreverNoCSV = csv.writer(csvfile) # a variável que vai ficar no lugar
        
        guardarPrimeiraPessoa = True
        # comparação boleana para colocar o indice na lista csv e ao mesmo tempo já adicionar 
        # o primeiro nome no arquivo csv assim que rodar o primeiro loop
        
        for pessoa in ListaObjeto:
            
            if guardarPrimeiraPessoa: # comparação boleana
                escreverNoCSV.writerow([ "nome" , "idade" ])
                guardarPrimeiraPessoa = False # a variável ganhar valor False para não reptetir novamente.
            
            name = pessoa.getNome()
            idade = pessoa.getIdade() 
            escreverNoCSV.writerow([name,idade])

def trazerObjetosCSV():
    # retorna a lista do csv
    
    listaPessoasDoCSV = []
    with open(caminho) as csvfile:
        csvfile = csv.reader(csvfile, delimiter=",")
        for pessoa in (csvfile):
                retornaObJ = Pessoa( pessoa[0] , pessoa[1] )
                listaPessoasDoCSV.append(retornaObJ)    
    
    listaPessoasDoCSV.pop(0)
    return listaPessoasDoCSV


# início objetos criados
pedro = Pessoa("Pedro",28)
carla = Pessoa("Carla",35)
john = Pessoa("John",18)
paulo = Pessoa("Paulo",30)
tico = Pessoa("Tico",45)
teco = Pessoa("Teco",10)
zorro = Pessoa("Zorro", 75)
# fim objetos criados

# adicionar objetos na lista.
listaDePessoas =[tico,pedro,carla,john,paulo,teco,zorro]

levarObjetoParaCSV(listaDePessoas)

ObjetosDoCSV = trazerObjetosCSV()

rodarIf = True
for elemento in ObjetosDoCSV:
    
    if rodarIf:
        print("Nome | idade ")
        rodarIf = False

    print(elemento.getNome(),elemento.getIdade())
