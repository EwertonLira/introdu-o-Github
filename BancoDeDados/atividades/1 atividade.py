import csv

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
    # melhorar: 1 ele manda uma lista vazia e cheia alternadamente
    # melhorar: 2 ele não manda os indices em asplas duplas.
    
    with open('atividades/pessoas.csv', 'w') as csvfile:
        for titulo in range(1):
            csv.writer(csvfile, delimiter=',').writerow([ '\"name\"', '\"idade\"' ]) # não está deixando passar o texto entre aspas duplas.
            for pessoa in ListaObjeto:
                name = pessoa.getNome()
                idade = pessoa.getIdade() 
                csv.writer(csvfile, delimiter=',').writerow([name,idade])

def trazerObjetosCSV():
    # retorna a lista do csv
    
    listaPessoasDoCSV = []
    with open("atividades/pessoas.csv") as csvfile:
        csvfile = csv.reader(csvfile, delimiter=",")
        for pessoa in (csvfile):
            if pessoa:
                retornaObJ = Pessoa( pessoa[0] , pessoa[1] )
                listaPessoasDoCSV.append(retornaObJ)
            else:
                pass              
    
    return listaPessoasDoCSV


# início objetos criados
pedro = Pessoa("Pedro",28)
carla = Pessoa("Carla",35)
john = Pessoa("John",18)
paulo = Pessoa("Paulo",30)
tico = Pessoa("Tico",45)
teco = Pessoa("Teco",10)
# fim objetos criados

# adicionar objetos na lista.
listaDePessoas =[tico,pedro,carla,john,paulo,teco]

levarObjetoParaCSV(listaDePessoas)

ObjetosDoCSV = trazerObjetosCSV()

for elemento in ObjetosDoCSV:
    print(elemento.getNome(),elemento.getIdade())
