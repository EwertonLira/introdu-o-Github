# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def apresentar(self):
#        print(f"Olá meu nome é {self.nome}!")
       
    
#     def apresentar_idade(self):
#         print(f"Olá minha idade é {self.idade}!")
        

# pessoa1 = Pessoa("Maria", 30)
# pessoa1.apresentar()
# pessoa1.apresentar_idade()

# class Circulo:
#     def __init__(self,raio):
#         self.raio = raio

#     def area(self):
#         area = 3.14 * (self.raio**2)
#         return area

# circulo = Circulo(5)
# print(circulo.area())
'''''''''
class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def informacoes(self):
        print(f'{self.titulo} - {self.autor} ({self.ano}).')

livro1 = Livro('O senhor dos anéis','J. R. R. Tolkien','1954')
livro1.informacoes()
''''''''''''
class Funcionario:
    def __init__(self,nome,salario,departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento
    
    def aumentarSalario(self):
        self.salario = self.salario+(self.salario/100)*10
        return self.salario
   
    def informacoes(self):
        print(f'{self.nome} - {self.departamento},{self.salario}).')
pessoa1 = Funcionario("Joao",3000,"Vendas")
pessoa1.aumentarSalario()
pessoa1.informacoes()


'''

class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def informacoes(self):
        print (self.modelo, "-", self.marca, "-", self.ano)

    def acelerar(self):
        velocidade = "80 Km / h"
        return velocidade

carro1 = Carro("Uno","Fiat","2000")
carro1.informacoes()
print(f'o carro {carro1.modelo} {carro1.marca} acelerou para',carro1.acelerar())