# Criar método de batalha onde dois pokemons, lutam e é determinado o
# vencedor. Os turnos da batalha e seu resultado devem ser impressos no
# terminal. O pokemon do jogador deve ser escolhido pelo próprio com
# base na sua lista de pokemons, o pokemon do Inimigo deve ser escolhido
# aleatoriamente (usar a biblioteca random) (tudo feito)

import random
import json

class Pokemon: # 1. modelar Classe Pokemon (feito)
    def __init__(self,apelido,
        name,hp,attack,defense,spAttack,spDefense,Speed,
        type1,type2):

        self._apelido = apelido # não utilizado
        self._level = random.randint(1,50)
        self._name = name
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._spAttack = spAttack #sp abreviação de especial
        self._spDefense = spDefense
        self._speed = Speed
        self._movePoke = []
        self._type1 = type1
        self._type2 = type2

    # início métodos gets.
    def getLevel(self):
        return self._level
    def getName(self):
        return self._name
    def getHp(self):
        return self._hp
    def getAttack(self):
        return self._attack
    def getDefense(self):
        return self._defense
    def getSpAttack(self):
        return self._spAttack
    def getSpDefense(self):
        return self._spDefense
    def getSpeed(self):
        return self._speed
    def getMovePoke(self):
        return self._movePoke
    def getType1(self):
        return self._type1
    def getType2(self):
        valor = self._type2
        valor.upper()
        return valor

    def critico(self):
        ale = random.random()
        if ale > 0.95:
            ValorCritico = 2.5
        elif ale > 0.70:
            ValorCritico = 1.5
        else:
            ValorCritico = 1
        
        return ValorCritico

    def _chamarListaPoke(self):
        with open("poke/poke.json", 'r') as pokemonjson:
            lista = json.load(pokemonjson)

            return lista

    def ovoPoke(self):
        ovo = random.choice(self._chamarListaPoke())
        chocarOvo = dict(ovo)
        return chocarOvo

    def _chamarMovePoke(self):
        with open("habilidades/movePoke.json", 'r') as movePokejson:
            lista = json.load(movePokejson)

            return lista

    def movimentoPoke(self):
        move = random.choice(self._chamarMovePoke())
        movimento = dict(move)
        return movimento
    # fim métodos gets.
    
    # métodos sets.
    def setMovePoke(self,move):
        self._movePoke.append(move)

    

