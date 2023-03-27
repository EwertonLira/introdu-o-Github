from classPokemon import Pokemon


class PokemonEletrico(Pokemon):
    def __init__(self, nome, hp, atk, defesa):
        super().__init__(nome, hp, atk, defesa)
        self.tipo = "Elétrico"
