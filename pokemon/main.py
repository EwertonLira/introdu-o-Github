#14 separar o código em arquivos diferentes ... (incompleto)
from Treinador import *
from subClassePokemon import *
    
print("""
recomendado: aumente a tela do seu terminal.

Seja bem vindo ao jogo Pokémon
escreva o nome do jogador: 
""")
nomeTreinador = input("<(º.º)> ")
user1 = desafiante(nomeTreinador)

limparTela()
sleep(0.50)

print(f"""
{user1.getName()},
Escolha o seu primeiro Pokémon!
tecle uma das opções.
""")

listaPrimeiroPoke = []
listaLetra = ["[a]","[s]","[d]"]
auxilar = SubClassePokemon(0,0,0,0,0,0,0,0,0,0)
contador = 0
for posicao in listaLetra:
    listaPrimeiroPoke.append(auxilar.ovoPoke())
    textoName = listaPrimeiroPoke[contador]["Name"]
    contador += 1
    print(f"{posicao}. {textoName}")

letra = ""
while not(letra) in ["a","s","d"]:
    letra = input("<(º.º)> ")
    
limparTela()
sleep(0.70)

match letra:
    case "a":
        posicaoDaLista = 0
    case "s":
        posicaoDaLista = 1
    case "d":
        posicaoDaLista = 2

aux1 = listaPrimeiroPoke[posicaoDaLista]
poke1 = SubClassePokemon(None,aux1['Name'],aux1['HP'],aux1['Attack'],aux1['Defense'],aux1['Sp. Atk'],aux1['Sp. Def'],aux1['Speed'],aux1["Type 1"],aux1["Type 2"])
user1.setCapturarPokemon(poke1)

print("<(º.º)> carregando...")
contador = 0 # 10 incluir uso de pelo menos 1 laço de repetição (for ou While) (feito)
while contador < 3:
    moveAux = auxilar.movimentoPoke()
    mov = moveAux["Type"]
    tipoAux = poke1.getType1()
    tipoAux = tipoAux.upper()
    logico = mov == tipoAux
    if logico: # 11. incluir uso de pelo menos 1 estrutura condiciona simples (if) ou ... (feito)
        poke1.setMovePoke(moveAux)
        contador += 1
    

opcao= ""
while (opcao != "f"): # 13 Envolver tudo em um loop em que o programa é exectuado ... (feito)
    limparTela()
    sleep(0.50)
    print(f"""
    Escolha uma das opções:

    [a] - Exibir seus Pokémons
    [s] - Capturar Pokémon
    [d] - Procurar batalha Pokémon
    [f] - Sair
    """)
    opcao = input("<(º.º)> ") 
    match opcao: #12 criar um menu para o jogador... (feito)
        case "a":
            
            sleep(0.50)
            limparTela()
            print("Seus pokemons, capacidade total:3")
            print(user1.getMochilaPokemon())
            input("<(º.º)> ")
        case "s":
           
            sleep(0.50)
            limparTela()
            if user1.getMochilaPokemon() <= 2:
                limparTela()
                novoPoke = auxilar.ovoPoke()
                texto = novoPoke["Name"]
                print(f"""
                Você encontrou um {texto} deseja capturar?
                escreva [s] para sim ou [n] para não.
                """)
                SN = input("<(º.º)> ")
                if SN in ["s","S"]:
                    pok = SubClassePokemon(None,novoPoke['Name'],novoPoke['HP'],novoPoke['Attack'],novoPoke['Defense'],novoPoke['Sp. Atk'],novoPoke['Sp. Def'],novoPoke['Speed'],novoPoke["Type 1"],novoPoke["Type 2"])
                    user1.setCapturarPokemon(pok)
                    print("pokemom capturado!")
                    input("<(º.º)> ")
                    
                    print("<(º.º)> carregando...")
                    contador = 0
                    while contador < 3:
                        moveAux = auxilar.movimentoPoke()
                        mov = moveAux["Type"]
                        tipoAux = pok.getType1()
                        tipoAux = tipoAux.upper()
                        logico = mov == tipoAux
                        if logico:
                            pok.setMovePoke(moveAux)
                            contador += 1
                   
                elif SN in ["n","N"]:
                    print(f"""
                    você deixou de capturar o pokemon
                    {novoPoke['Name']}
                        """)
                    input("<(º.º)> ")
                    
            else:
                print("""
                a sua mochila está cheia. Deseja abandonar um pokemon?
                escreva [s] para sim ou [n] para não.
                """)
                SN = input("<(º.º)> ")
                if SN in ["s","S"]:
                    user1.getMochilaPokemon()
                    print("""escolha o seu primeiro, segundo ou terceiro pokemon:
                    tecle [1],[2] ou [3]""")
                    valor = input("<(º.º)> ")
                    if valor in ["1","2","3"]:
                        match valor:
                            case "1":
                                valorf = 0
                            case "2":
                                valorf = 1
                            case "3":
                                valorf = 2
                            case _:
                                print("""
                                seus pokemons estão felizes porque você não
                                abadonou nenhum deles. tente novamente se digitou algo errado.
                                """)
                        user1.setRemovePokemon(int(valorf))
                        print("pokemom removido")
                        input("<(º.º)> ")
                    else:
                        print("""
                            seus pokemons estão felizes porque você não abadonou nenhum deles.
                            tente novamente se digitou algo errado.
                            """)
                        input("<(º.º)> ")
                else:
                    print("Seus pokemons agradecem a sua decisão")
                    input("<(º.º)> ")
        case "d":
            aux2 = auxilar.ovoPoke()
            pokeOponente = SubClassePokemon("pokémon selvagem",aux2['Name'],aux2['HP'],aux2['Attack'],aux2['Defense'],aux2['Sp. Atk'],aux2['Sp. Def'],aux2['Speed'],aux2["Type 1"],aux2["Type 2"])
            oponenteCaptura = Oponente(True)
            opName = oponenteCaptura.getName()
            oponenteCaptura.setCapturarPokemon(pokeOponente)
            print(f"""
            {user1.getName()}, treinador(a) {opName} com
            o pokémon {pokeOponente.getName()} que batalhar.
            Deseja batalhar com ele(a):
            escreva [s] para sim ou [n] para não.
            """)
            SN = input("<(º.º)> ")
            if SN in ["s","S"]:
                limparTela()
                user1.getMochilaPokemon() # 8. permitir que o jogador escolha o pokemom (feito)
                print("""
                Escolha o seu primeiro, segundo ou 
                terceiro pokémon para batalhar:
                tecle [1],[2] ou [3]
                """)
                valor = input("<(º.º)> ")
                if valor in ["1","2","3"]:
                    match valor:
                        case "1":
                            valorf = 0
                        case "2":
                            valorf = 1
                        case "3":
                            valorf = 2
                        case _:
                            print("""
                            Seus pokémons estão querendo entrar em ação.
                            tente novamente se digitou algo errado.
                            """)
                    try:
                        pokelutar = user1.chamarPokemonBatalha(int(valorf))
                        pokelutar.metodoDebatalha(pokeOponente,user1,opName)
                        input("<(º.º)> ")
                    except:
                        qtd = user1.getMochilaPokemon()
                        print(f"Você tem apenas {qtd} pokémons. tente novamente")
                        input("<(º.º)> ")
                else:
                    print("""
                        Seus pokémons estavam prontos, mas a batalha não aconteceu.
                        tente novamente se digitou algo errado.
                        """)
                    input("<(º.º)> ")
            else:
                print("Seus pokémons querem lutar!")
                input("<(º.º)> ")     
        case "f":
            print("Obrigado por Jogar!")
            sleep(1.5)
            limparTela()
            
        
                
                
