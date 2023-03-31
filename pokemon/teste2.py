from os import system, name 
from time import sleep 
def limparTela(): 
    
    if name == 'nt': 
        _ = system('cls') 
      
    else: 
        _ = system('clear') 

fire = {"ordem": 2,"name":"fire"}
grass = {"ordem": 3,"name":"grass"}
Pound = {"ordem": 1,"name":"Pound","descrição":"Nenhum","atkPower":40,"acerto":100,"pp":35,"tipo":"normal"}
getMove = [Pound,fire,grass]

def menuDeMeuMovimento(): #função precisa importar  limparTela() e sleep() e retorna um número da opção, usa dicionário.
    
    rodarWhile = True

    while rodarWhile:
        
        print("Escolha o movimento do  seu pokemon")
        for numeroDaLista, MoveDaLista in enumerate(getMove,1):
            print(f"[{numeroDaLista}] {MoveDaLista}")
        print("[0] voltar")
        
        opcaoDeMove = input(": ")
        
        if opcaoDeMove in ["0"]:
            valorRetorno = False
            rodarWhile = False
        
        elif opcaoDeMove in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:
            buscarMove = int(opcaoDeMove)
           
            match buscarMove:
                case 1:
                    valorRetorno = getMove[0]
                case 2:
                    valorRetorno = getMove[1]
                case 3:
                    valorRetorno = getMove[2]
                case 4:
                    valorRetorno = getMove[3]
                case 5:
                    valorRetorno = getMove[4]
                case 6:
                    valorRetorno = getMove[5]
                case 7:
                    valorRetorno = getMove[6]
                case 8:
                    valorRetorno = getMove[7]
                case 9:
                    valorRetorno = getMove[8]
                case 10:
                    valorRetorno = getMove[9]
                case 11:
                    valorRetorno = getMove[10]
                case 12:
                    valorRetorno = getMove[11]
                case 13:
                    valorRetorno = getMove[12]
                case 14:
                    valorRetorno = getMove[13]
                case 15:
                    valorRetorno = getMove[14]
            rodarWhile = False
        else:
            print("opção invalida")
            sleep(1) 
            limparTela()
    
    return valorRetorno

def calculoDeDano(level,spAttack,atkPower,spDefense,stab,weaknessResistance,critical,other,margin):
    dano = ((((2*level/5+2)*spAttack*atkPower/spDefense)/50)+2)*stab*weaknessResistance*critical*other*(margin/100)
    return dano

def metodoDebatalha():
    desafianteHp = 120
    oponenteHp = 150
    
    
    #posso colocar todos os atributos aqui.
    #desafianteHp = self.getHp()
    #oponenteHp = oponente.getHp()
    getSpeed = 7
    oponentegetSpeed = 5
    
    while (desafianteHp or oponenteHp <= 0):

        if getSpeed > oponentegetSpeed:
            print("desafiante começa")
            print(f""" escolha uma das opções:
            [A]attack
            [S]spMove
            [D]Item
            [Z]desistir
            {oponenteHp}
            """)
            opcoesDeJogada = input("Insira um valor")
            match opcoesDeJogada:
                case "a": # ataque normal
                    porrada = calculoDeDano(2,45,Bp,45,1.5,1.5,1.5,1.5,88)
                    oponenteHp -= porrada
                case "s": # movimento especial de ataque.
                    meuMove =  menuDeMeuMovimento()
                    Bp = meuMove["atkPower"]
                    porrada = calculoDeDano(2,45,Bp,45,1.5,1.5,1.5,1.5,88)
                    oponenteHp -= porrada
                case "d":
                    # menuDeMeuItem()
                    pass
                case "z":
                    print("Você tem certeza que deseja desistir?")
                    opcao = input("""
                    tecle [S] para sim
                    tecle [N] para não
                    : 
                    """)
                    if opcao in ["s","S","n","N"]:
                        if opcao in ["s","S"]:
                            print("Você perdeu por W.O")
                            # gerar exp
                            desafianteHp = 0 
                        else:
                            pass
                    else:
                        print("comando inválido")
        
        # random() na lista de ataquee: ataque do inimigo
        
        if  desafianteHp or oponenteHp <= 0:
            if desafianteHp and oponenteHp <= 0:
                if desafianteHp > oponenteHp:
                    vencendorDaBatalha = "desafiante"
                else:
                    vencendorDaBatalha = "oponente"
            elif desafianteHp <= 0:
                vencendorDaBatalha = "oponente"
            else:
                vencendorDaBatalha = "desafiante"
        else: # se não um deles não for menor que zero vai continuar:
            pass
    
    return vencendorDaBatalha


metodoDebatalha()