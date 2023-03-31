# Criar método de batalha onde dois pokemons, lutam e é determinado o
# vencedor. Os turnos da batalha e seu resultado devem ser impressos no
# terminal. O pokemon do jogador deve ser escolhido pelo próprio com
# base na sua lista de pokemons, o pokemon do Inimigo deve ser escolhido
# aleatoriamente (usar a biblioteca random)

# dar uma olhada
#https://pokemondb.net/move/all


#________________________________

# level de ambos os pokemons? (caso naõ entender, necessário usar média)
# spAttack = ataque especial
# atkPower = base power (bP) = o pontos do dano do movimento
# spDefense = defesa especial do pokemom que vai receber o golpe.
# stab = bônus de golpe do mesmo tipo (Same-Type Attack Bônus)
# weaknessResistance = é a variável de fraqueza ou resistência do defensor, que pode ser entre 0, 0,25, 0,5, 1, 2 e 4;
# critical = é o valor para critical hits; seu valor será 1,5 para golpes críticos e 1 para golpes normais.
# other = é a variável para itens, habilidades, efeito de Burn, etc. O valor que você vai colocar dependerá da situação. Por exemplo, você colocaria x1,3 (30%) caso o atacante estivesse segurando Life Orb.
# margin = é uma variável de margem de erro; se quiser o dano mínimo que este golpe causará, use 80. Para o máximo, use 100.

def calculoDeDano(level,spAttack,atkPower,spDefense,stab,weaknessResistance,critical,other,margin):
    dano = ((((2*level/5+2)*spAttack*atkPower/spDefense)/50)+2)*stab*weaknessResistance*critical*other*(margin/100)
    return dano

def statsModifiers(atributo,levelModificador):   
    match levelModificador:
        case -6:
            valor = 0.25 # ou 25%
        case -5:
            valor = 0.29 # ou 29%
        case -4:
            valor = 0.33 # ou 33%
        case -3:
            valor = 0.40 # ou 40%
        case -2:
            valor = 0.50 # ou 50%
        case -1:
            valor = 0.66 # ou 66%
        case 0:
            valor = 1    # ou 100%
        case 1:
            valor = 1.5  # ou 150%
        case 2:
            valor = 2    # ou 200%
        case 3:
            valor = 2.5  # ou 250%
        case 4:
            valor = 3    # ou 300%
        case 5:
            valor = 3.5  #  ou 350%
        case 6:
            valor = 4    # ou 400%
        
    return atributo * valor

def menuDeMeuMovimento(): #função precisa importar  limparTela() e sleep() e retorna um número da opção, usa lista.
    rodarWhile = True
    while rodarWhile:
        print("Escolha o movimento do  seu pokemon")
        for numeroDaLista, MoveDaLista in enumerate(self.getMove(),1):
            print(f"[{numeroDaLista}] {MoveDaLista}")
        
        print("[0] voltar")
        opcaoDeMove = input(": ")
        if opcaoDeMove in ["0"]:
            valorRetorno = False
            rodarWhile = False
        elif opcaoDeMove in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
            valorRetorno = int(opcaoDeMove)
            rodarWhile = False
        else:
            print("opção invalida")
            sleep(1) 
            limparTela()
    
    return valorRetorno



def getMove(self):
    return self.Move() # movimentos listas
    
    



def metodoDebatalha():
    desafianteHp = self.getHp()
    oponenteHp = oponente.getHp()
    #posso colocar todos os atributos aqui.
    desafianteHp = self.getHp()
    oponenteHp = oponente.getHp()



    if self.getSpeed() > oponente.getSpeed():
        print("desafiante começa")
        print(""" escolha uma das opções:
        [A]attack
        [S]spMove
        [D]Item
        [Z]desistir
        """)
        match opcoesDeJogada:
            case attack:
               oponenteHp = (
                calculoDeDano(self.getLevel(), self.getAttack(), self.getAttack(), self.getDefense(), self.getStab(), self.getWeaknessResistance(), self.getCritical(), self.getOther(), self.getMargin()) 
                - oponenteHp) #atkPower ou Bp no ataque físico irei usar o mesmo ponto de ataque.
            
            case spMove: # movimento especial de ataque.
                    menuDeMeuMovimento()

                
                #>>> fazer o oponente receber status (poison exemplo.) se tiver.
                
                
                
                oponenteHp = (
                calculoDeDano(self.getLevel(), self.getSpAttack(), self.getAtkPower(), self.getDefense(), self.getStab(), self.getWeaknessResistance(), self.getCritical(), self.getOther(), self.getMargin())
                - oponenteHp ) #atkPower ou Bp no ataque spMove irei usar pontos de poder do movimento.
                self.setPp()
            case item:
                #>>> colocar item no pokémon
            case desistir:
                #>>> sair da batalha.

