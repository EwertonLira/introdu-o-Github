# Crie uma classe chamada Pokemon. Tente imaginar os
# atributos que um objeto dessa classe teria.
# Faça um programa que instância um objeto da classe
# Pokemon e imprima os atributos desse objeto.
# Bônus: Crie 2 objetos Pokemon e tente criar uma função
# de batalha que recebe os 2 objetos e determine quem sai
# ganhando.

class Pokemon:
    def __init__(self,nome, tipo, mover, vida, poder): # __init__ é o contrutor
        self.nome = nome
        self.tipo = tipo
        self.mover = mover
        self.vida = vida
        self.poder = poder
    
    def informacoesPokemon(self):
        print(f"""
        Nome: {self.nome}
        tipo: {self.tipo}
        movimentação: {self.mover}
        vida: {self.vida}
        poder: {self.poder}
        """)
    
    
        

pokemon1 = Pokemon("Pikachu","elétrico","rápido",120,80)
pokemon2 = Pokemon("Bulbasauro","Planta","médio",240,50)

pokemon1.informacoesPokemon()
pokemon2.informacoesPokemon()

