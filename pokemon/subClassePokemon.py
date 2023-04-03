from classPokemon import *
from funcoes import *

class SubClassePokemon(Pokemon): #modelar pelo menos 3 subclasses de pokemom com base no seu tipo (não feito)
    def __init__(self, apelido, name, hp, attack, defense, spAttack, spDefense, Speed, type1, type2):
        super().__init__(apelido, name, hp, attack, defense, spAttack, spDefense, Speed, type1, type2)


    def AcertividadeTotalDoDano(self): # método para gerar uma taxa de acertividae do dano causado
        valor = random.randint(80,100)
        return valor

    def menuDeMeuMovimento(self): #gera a lista de habilidades pokemom para o usuário escolher
        rodarWhile = True
        while rodarWhile:
            print("Escolha o movimento do  seu pokémon")
            for numeroDaLista, MoveDaLista in enumerate(self.getMovePoke(),1):
                texto = MoveDaLista["Name"]
                print(f"[{numeroDaLista}] {texto}")
            
            opcaoDeMove = input("<(º.º)> ")
            if opcaoDeMove in ["1","2","3"]:
                match opcaoDeMove:
                    case "1":
                        valorRetorno = 0
                    case "2":
                        valorRetorno = 1
                    case "3":
                        valorRetorno = 2
                
                rodarWhile = False
            else:
                print("<(º.º)> opção invalida")
        
        return valorRetorno

    def verificarVencendor(self,hpdesafiante, valorDoHpOponente,pokeOponente,usuario,opName): # verificar quem ganhou a batalha com base o hp
        if  valorDoHpOponente <= 0:  
            print(f"Treinador(a) {usuario.getName()} com o pokémon {self.getName()} ganhou a batalha!")
            return True

        elif hpdesafiante <= 0:
            print(f"Treinador(a) {opName} com o {pokeOponente.getName()} ganhou a batalha!")
            return True
        
        else:
            pass

    def metodoDebatalha(self, pokeOponente,usuario,opName): #5 Criar método de batalha onde dois pokemons, lutam.... (feito)
        # hp do desafiante (usuário)
        desafianteHp = int(self.getHp())
        desafianteHp += (self.getLevel()*(desafianteHp/50))

        # hp do oponente
        oponenteHp = int(pokeOponente.getHp())
        oponenteHp += (150 + (self.getLevel()*(oponenteHp/50)))

        # texto de abertura da batalha
        print("")
        sleep(0.75)
        print(f"{self.getName()}")
        sleep(0.75)
        print(f"VS")
        sleep(0.75)
        print(f"{pokeOponente.getName()}")
        sleep(0.75)
        limparTela()

        #while para rodar a batalha a até um dos hp chegar a zero.
        rodarWhile = True
        while rodarWhile:
           
            # verifica a cada golpe quem é o ganhador
            indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
            if indice:
                break

            # quem tiver o maior speed começa a batalha
           
            if self.getSpeed() > pokeOponente.getSpeed():
                # jogador quando começa a atacar
                print(f"""
                {usuario.getName()}, escolha uma das opções que deseja realizar:
                {self.getName()}: HP {desafianteHp:.0f}
                VS
                {pokeOponente.getName()}: HP {oponenteHp:.0f}

                [A] Atacar 
                [S] Habilidade especial
                [Z] Desistir
                """)
                
                opcoesDeJogada = ""
                while not(opcoesDeJogada) in ["a","s","z"]:
                    opcoesDeJogada = input("<(º.º)> ")

                limparTela()

                match opcoesDeJogada:
                    
                    case "a": # ataque normal
                        levD = self.getLevel()
                        atkD = self.getAttack()
                        criD = self.critico()
                        defO = pokeOponente.getDefense()
                        aceD = self.AcertividadeTotalDoDano()             
                        porrada = calculoDeDano(levD,atkD,atkD,defO,1,1,criD,1.5,aceD)
                        oponenteHp -= porrada
                        
                        print(f"""
                        pokémon {self.getName()} atacou o
                        {pokeOponente.getName()} com {porrada:.0f} de Dano.""")
                        input("<(º.º)> ")
                        limparTela()

                        indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
                        if indice:
                           break

                        # inicio ataque oponete 
                        levO = pokeOponente.getLevel()
                        atkO = pokeOponente.getAttack()
                        criO = pokeOponente.critico()
                        defD = self.getDefense()
                        aceO = self.AcertividadeTotalDoDano()  
                        porrada = calculoDeDano(levO,atkO,atkO,defD,1,1,criO,1.5,aceO)
                        desafianteHp -= porrada
                        
                        print(f"""
                        pokémon {pokeOponente.getName()} atacou o
                        {self.getName()} com {porrada:.0f} de Dano.""")
                        input("<(º.º)> ")
                        limparTela()
                        
                        # fim ataque oponete

                        indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
                        if indice:
                            break

                    case "s": # movimento especial de ataque do jogador
                        
                        # inicio tratamento da informação que vem do banco de dados
                        meuMoveindice =  self.menuDeMeuMovimento()
                        moveEscolhido =self.getMovePoke()[meuMoveindice]
                        valor = moveEscolhido['Power']
                        try:
                            valorTratado = int(valor)
                        except:
                            valorTratado = self.getAttack()
                        # fim  tratamento da informação que vem do banco de dados
                        
                        # variaveis para calcular o dano especial
                        Bp = valorTratado
                        levD = self.getLevel()
                        atkD = self.getAttack()
                        criD = self.critico()
                        defO = pokeOponente.getDefense()
                        aceD = self.AcertividadeTotalDoDano()  
                        porrada = calculoDeDano(levD,atkD,Bp,defO,1.2,1.2,criD,1.5,aceD)
                        oponenteHp -= porrada
                        
                        print(f"""
                        pokémon {self.getName()} atacou o
                        {pokeOponente.getName()} com o movimento {moveEscolhido['Name']}
                        acertou {porrada:.0f} de Dano.""")
                        input("<(º.º)> ")
                        limparTela()
                        
                        indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
                        if indice:
                            break

                        # oponente ataca nessa parte do código.
                        levO = pokeOponente.getLevel()
                        atkO = pokeOponente.getAttack()
                        criO = pokeOponente.critico()
                        defD = self.getDefense()
                        aceO = self.AcertividadeTotalDoDano()  
                        porrada = calculoDeDano(levO,atkO,atkO,defD,1.5,1.5,criO,1.5,aceO)
                        desafianteHp -= porrada
                        
                        print(f"""
                        pokémon {pokeOponente.getName()} atacou o
                        {self.getName()} com {porrada:.0f} de Dano.
                        """)
                        input("<(º.º)> ")
                        limparTela()
                        
                        indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
                        if indice:
                            break

                    case "z": # comando pra sair da batalha
                        print("Você tem certeza que deseja desistir?")
                        opcao = input("""
                        tecle [S] para sim
                        tecle [N] para não
                        >
                        """)
                        if opcao in ["s","S","n","N"]:
                            if opcao in ["s","S"]:
                                print("Você abandou a partida")
                                # gerar exp
                                desafianteHp = 0 
                            else:
                                pass
                        else:
                            print("comando inválido")
            else:  # o oponente começa atacando.
                               
                print(f"""
                {self.getName()}: HP {desafianteHp:.0f}
                VS
                {pokeOponente.getName()}: HP {oponenteHp:.0f}
                """)
                
                levO = pokeOponente.getLevel()
                atkO = pokeOponente.getAttack()
                criO = pokeOponente.critico()
                defD = self.getDefense()
                aceO = self.AcertividadeTotalDoDano()  
                porrada = calculoDeDano(levO,atkO,atkO,defD,1,1,criO,1.5,aceO)
                desafianteHp -= porrada
               
                print(f"""
                pokémon {pokeOponente.getName()} atacou o
                {self.getName()} com {porrada:.0f} de Dano.""")
                input("<(º.º)> ")
                limparTela()

                indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
                if indice:
                    break

                # agora é a vez do jogador
                print(f"""
                {usuario.getName()}, escolha uma das opções que deseja realizar:
                {self.getName()}: HP {desafianteHp:.0f}
                VS
                {pokeOponente.getName()}: HP {oponenteHp:.0f}

                [A] Atacar 
                [S] Habilidade especial
                [Z] Desistir
                """)

                opcoesDeJogada = ""
                while not(opcoesDeJogada) in ["a","s","z"]:
                    opcoesDeJogada = input("<(º.º)> ")
                
                limparTela()
                
                match opcoesDeJogada:
                    case "a": # ataque normal
                        levD = self.getLevel()
                        atkD = self.getAttack()
                        criD = self.critico()
                        defO = pokeOponente.getDefense()
                        aceD = self.AcertividadeTotalDoDano()              
                        porrada = calculoDeDano(levD,atkD,atkD,defO,1,1,criD,1.5,aceD)
                        oponenteHp -= porrada
                        
                        print(f"""
                        pokémon {self.getName()} atacou o
                        {pokeOponente.getName()} com {porrada:.0f} de Dano.""")
                        input("<(º.º)> ")
                        
                        limparTela()

                        indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
                        if indice:
                            break
                    
                    case "s": # movimento especial de ataque.
                       # inicio tratamento da informação que vem do banco de dados
                        meuMoveindice =  self.menuDeMeuMovimento()
                        moveEscolhido =self.getMovePoke()[meuMoveindice]
                        valor = moveEscolhido['Power']
                        try:
                            valorTratado = int(valor)
                        except:
                            valorTratado = self.getAttack()
                        # fim  tratamento da informação que vem do banco de dados
                        
                        # variaveis para calcular o dano especial
                        Bp = valorTratado
                        levD = self.getLevel()
                        atkD = self.getAttack()
                        criD = self.critico()
                        defO = pokeOponente.getDefense()
                        aceD = self.AcertividadeTotalDoDano()  
                        porrada = calculoDeDano(levD,atkD,Bp,defO,1.2,1.2,criD,1.5,aceD)
                        oponenteHp -= porrada
                        
                        print(f"""
                        pokémon {self.getName()} atacou o
                        {pokeOponente.getName()} com o movimento {moveEscolhido['Name']}
                        acertou {porrada:.0f} de Dano.""")
                        input("<(º.º)> ")
                        limparTela()
                        
                        indice = self.verificarVencendor(desafianteHp,oponenteHp,pokeOponente,usuario,opName)
                        if indice:
                            break

                    case "z": # comando para sair da batalha
                        print("Você tem certeza que deseja desistir?")
                        opcao = input("""
                        tecle [S] para sim
                        tecle [N] para não
                        >
                        """)
                        if opcao in ["s","S","n","N"]:
                            if opcao in ["s","S"]:
                                print("Você abandou a partida")
                                # gerar exp
                                desafianteHp = 0 
                            else:
                                pass
                        else:
                            print("comando inválido")

           
