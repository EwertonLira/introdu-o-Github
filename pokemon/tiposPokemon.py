from classPokemon import Pokemon

class PokemonFogo(Pokemon):
    def __init__(self, nome, hp, atk, defesa):
        super().__init__(nome, hp, atk, defesa)
        self.tipo = "Fogo"

class PokemonAgua(Pokemon):
    def __init__(self, nome, hp, atk, defesa):
        super().__init__(nome, hp, atk, defesa)
        self.tipo = "Água"

class PokemonEletrico(Pokemon):
    def __init__(self, nome, hp, atk, defesa):
        super().__init__(nome, hp, atk, defesa)
        self.tipo = "Elétrico"

toto = PokemonFogo("chamander",100,120,255)
bel = PokemonAgua("tartaruga ninja",110,120,155)
teco = PokemonEletrico("pikachu",200,155,150)

teco.lutar(bel)
bel.lutar(toto)
toto.lutar(teco)

