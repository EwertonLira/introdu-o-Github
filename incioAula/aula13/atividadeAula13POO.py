# class Carro:
#     def __init__(self,marca,modelo,ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
    
#     def informacoes(self):
#         print(f"{self.marca} - {self.modelo} - {self.ano}.")
    
#     def acelerar(self,aceleracao):
#         print(F"O {self.marca} {self.modelo} acelerou para {aceleracao} km/h.")

# carro = Carro("Fiat","Uno",2000)

# carro.informacoes()
# carro.acelerar(80)

######################################

class Agenda:
    def __init__(self,listaContato,NumMaxContatoPerm):
        self.listaContato = listaContato
        self.NumMaxContatoPerm = NumMaxContatoPerm


    def adicionar_contato(self,contatoAdd):
        if len(self.listaContato) <= self.NumMaxContatoPerm:
            self.listaContato.append(contatoAdd)
        else:    
            print(f"A listas está cheia, não é possiível adicionar {contatoAdd}.")

    def removerContato(self,nomeContato):
        for nomeDaLista in self.listaContato:
            if nomeDaLista.nome == nomeContato:
                self.listaContato.remove(nomeDaLista)

        
    def informacoes(self):
        mensagem = ""
        for itemDalista in self.listaContato:
            mensagem += f"{itemDalista.nome} - {itemDalista.telefone} \n"
        return mensagem
class Contato:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

pessoa1 = Contato("João",922224444)
pessoa3 = Contato("Paulo", 977771111)
pessoa2 = Contato("Pedro",988887777)

agenda1 = Agenda([],5)
agenda1.adicionar_contato(pessoa1)
agenda1.adicionar_contato(pessoa2)
agenda1.adicionar_contato(pessoa3)

print(agenda1.informacoes())

agenda1.removerContato("Pedro")

print(agenda1.informacoes())