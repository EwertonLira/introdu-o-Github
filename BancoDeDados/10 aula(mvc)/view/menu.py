# menu da aplicação
from model.main import *



def opçãoSair():
    print("Saindo do programa...")

def menu():

    while True:
        print('''
        🏪 loja 🏪

escolha uma das opções abaixo digitando
a letra correspondente e aperte [ENTER]
        
    [E] - cadastrar novo cliente
    [S] - ...
    [D] - ...
    [F] - ...
    [E] - ...
    [Q] - ...
    [Z] - sair
        ''')
        op = input(": ")

        match op:
            case "e" | "E":
                print()
                inserirCliente()
            case "s" | "S":
                pass
            case "d" | "D":
                pass
            case "f" | "F":
                pass
            case "e" | "E":
                pass
            case "q" | "Q":
                pass
            case "z" | "Z":
                opçãoSair()
                break
            case _:
                print("Opção inválida. Digite novamente!")

        input("Tecle enter para continuar.")
