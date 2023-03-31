from os import system, name 
from time import sleep 

def limparTela(): 
    
    if name == 'nt': 
        _ = system('cls') 
      
    else: 
        _ = system('clear') 



#arvore
print("seja bem vindo ao jogo pokemom")

rodarWhile = ""
while (rodarWhile != 5):
    print(f"""
    Escolha uma das opções:

    1- Capturar Pokemon
    2- Procurar batalha pokemon
    3- Exibir seus pokemons
    4- Curar pokemons
    5- Sair
    """)
    opcao = input(": ")
    match opcao:
        case "1":
            # metodo de capturar pokemom.
            pass 
        case "2":
            rodarWhileBatalha = True
            while rodarWhileBatalha:
                print(f"""
                você está lutando com /fulano/

                    local: arena caucaia
                    clima: quente
                    vento: rapido
                    
                    """)
                
                # objeto.metodoDebatalha(self,oponente)
                
                
