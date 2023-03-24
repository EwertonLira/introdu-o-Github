class Pokemon:
    def __init__(self,nome,hp,atk,defesa):
        self._nome = nome
        self._hp = hp
        self._atk = atk
        self._defesa = defesa
        self.total = sum([self.getHp(),self.getAtk(),self.getDefesa()]) 
    
    def getHp(self):
        return self._hp
    
    def getAtk(self):
        return self._atk
    
    def getDefesa(self):
        return self._defesa

    def lutar(self,oponente):
    #    if ( 
    #     sum([self.getHp(),self.getAtk(),self.getDefesa()]) 
    #     >
    #     sum([oponente.getHp(),oponente.getAtk(),oponente.getDefesa()])
    #     ):
        if self.total > oponente.total:
            print(f" o pokemon {self._nome} venceu!")
        else:
          print(f" o pokemon {oponente._nome} venceu!")

if __name__ == "__main__":
    pokemonbel = Pokemon("bel",100,120,150)
    pokemonful = Pokemon("ful",120,130,140)

    pokemonbel.lutar(pokemonful)

    


