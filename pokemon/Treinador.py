# Modelar Classe Treinador. Essa classe deve conter como atributo uma lista de Pokemons. (feito)
# Criar método para capturar um novo pokemon. (feito)
# Criar método para listar pokemons do Jogador. (feito)

from classPokemon import *
import random
class Treinador: # 3 modelar Classe Treinador. Essa classe deve conter como atributo uma lista de pokemons (feito)

    def __init__(self,name):
        self._name = name
        self._mochilaPokemon = [] # mochila pokemon é a lista para os pokemons
    
 # início métodos gets.
    def getName(self):
        return self._name
    
    def getMochilaPokemon(self): #7. metodo para listar os pokemons do usuário.
        for poke in range(len(self._mochilaPokemon)):
            print(f"""
                       nome {self._mochilaPokemon[poke].getName()}
                      level {self._mochilaPokemon[poke].getLevel()}
              tipo Primario {self._mochilaPokemon[poke].getType1()} 
            tipo Secundário {self._mochilaPokemon[poke].getType2()}  
                         HP {self._mochilaPokemon[poke].getHp()}
                     Ataque {self._mochilaPokemon[poke].getAttack()}
                     Defesa {self._mochilaPokemon[poke].getDefense()}
            Ataque Especial {self._mochilaPokemon[poke].getSpAttack()}
            Defesa Especial {self._mochilaPokemon[poke].getSpDefense()}
                 Velocidade {self._mochilaPokemon[poke].getSpeed()}
                """)
        
        return len(self._mochilaPokemon)
        
    def chamarPokemonBatalha(self,indice):
        return self._mochilaPokemon[indice]
    # fim métodos gets.    
   
    # início métodos sets
    def setName(self,novoNome):
        self._name = novoNome
    
    def setRemovePokemon(self,indice):
        self._mochilaPokemon.pop(indice)
    
    def setCapturarPokemon(self,poke): # 6. método para capturar pokemom (feito)
        if len(self._mochilaPokemon) <= 2:
            self._mochilaPokemon.append(poke)
        else:
            print("sua mochila está cheia, permitido apenas 3 pokemons")
    # fim métodos sets

class desafiante(Treinador): # sub classe treinador(jogador) criada (feito)
    def __init__(self, name):
        super().__init__(name)


class Oponente(Treinador): # sub classe treinador(inimigo)criada (feito)
    
    def __init__(self, name):
        super().__init__(name=random.choice([
        "Camila","Carla","João","Pedro","Inês","Vitor","Miguel","Rafael","Daniel",
        "Salomão","'PitBull'","Lecy","Carvalho","Ashe","Brock","Tina","Lucas","Teodoro",
        "Samila","Karine","Catarina","Joana","Geraldo","'Destruidor'","Hector","Jack",
        "Horácio","Jonathan","noob1234","proHacker","20pega70correr","OusadoSuper",
        "Santana","user547","Loren","Fábio","Azevedo","'morteRápida'","destruidor de Noob",
        ]))
