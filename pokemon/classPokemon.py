# Modelar Classe Pokemon

class Pokemon:
    def __init__(self,nome,
        hp,attack,defense,spAttack,spDefense,Speed
        ):

        self._nome = nome
        # atributos permanentes:
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._spAttack = spAttack #sp abreviação de especial
        self._spDefense = spDefense
        self._speed = Speed
        #self.total = sum([self.getHp(),self.getAtk(),self.getDefesa()])
        self._move
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

chamirlion = Pokemon("zeze",120,80,50,56,70,50)
print(chamirlion.getHp())
print(chamirlion.getSpAttack())
print(chamirlion.getSpDefense())
print(chamirlion.getSpAttack())
print(chamirlion.getSpeed())



    
    
    
#     # _____________________________________________________
#     #    if ( 
#     #     sum([self.getHp(),self.getAtk(),self.getDefesa()]) 
#     #     >
#     #     sum([oponente.getHp(),oponente.getAtk(),oponente.getDefesa()])
#     #     ):
#         if self.total > oponente.total:
#             print(f" o pokemon {self._nome} venceu!")
#         else:
#           print(f" o pokemon {oponente._nome} venceu!")

# if __name__ == "__main__":
#     pokemonbel = Pokemon("bel",100,120,150)
#     pokemonful = Pokemon("ful",120,130,140)

#     pokemonbel.lutar(pokemonful)

    


