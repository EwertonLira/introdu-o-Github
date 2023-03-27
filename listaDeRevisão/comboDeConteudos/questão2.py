# 2 Escreva uma função que receba como parâmetro
# uma string e verifique se a string é um palíndromo 
# (ou seja, pode ser lida da mesma forma de trás para frente). 
# Em seguida, utilize uma estrutura de repetição para solicitar
# ao usuário uma string, chame a função e imprima se a string é 
# um palíndromo ou não.

rodarWhile = True
rodarWhile1 = True

def palíndromo(palavra):
    if palavra == palavra[::-1]:
        msg = f"A palavra {palavra} é um palíndromo."
    else:
        msg = f"A palavra {palavra} não é um palíndromo."

    return msg

while rodarWhile:
    while rodarWhile1:
        palavraInput = input("Insira uma string: ")
        print("\n",palíndromo(palavraInput),"\n")
        rodarWhile1 = False

    print(f"deseja usar novamente a função?")
    rodarNovamente = input("Tecle [S]sim ou [N]não: ")
    if rodarNovamente in ["s","S","sim","Sim","n","N","não","Não","nao","Nao"]:
        if rodarNovamente in ["s","S","sim","Sim"]:
            rodarWhile1 = True
        else:
            print("Obrigado por ter usado a nossa função")
            rodarWhile = False
    else:
        print("comando inválido")