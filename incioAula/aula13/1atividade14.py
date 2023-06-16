# 1. Crie uma classe Animal que tenha os atributos nome e idade e o método emitir_som(). Crie também as classes Cachorro, Gato e Pato que herdem da classe Animal e sobrescrevam o método emitir_som() para retornar “au au”, “miau” e “quack” respectivamente. Crie alguns objetos dessas classes e teste o método emitir_som() em cada um.
class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def emitirSom(self):
        print(f"O {self.nome} faz (som do animal)")

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def emitirSom(self):
        print(f"O {self.nome} faz Au Au")

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def emitirSom(self):
        print(f"O {self.nome} faz Miau")

class Pato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def emitirSom(self):
        print(f"O {self.nome} faz quack quack")

meuCachorro = Cachorro("totó",5)
meuPato = Pato("Patolino",30)
meuGato = Gato("Tom",17)
# O método emitirSom() está fora do f-string e 
print(f"""
{meuCachorro.nome} idade:{meuCachorro.idade}
{meuCachorro.emitirSom()}

{meuPato.nome} idade:{meuPato.idade}
{meuPato.emitirSom()}

{meuGato.nome} idade:{meuGato.idade}
{meuGato.emitirSom()}
""")