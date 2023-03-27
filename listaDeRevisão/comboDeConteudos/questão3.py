# 3 Escreva uma função que receba como parâmetro 
# uma lista de strings e retorne a quantidade de strings
# que possuem mais de 5 caracteres. Em seguida, utilize uma 
# estrutura condicional para perguntar ao usuário se ele deseja
# adicionar mais strings à lista, e utilize um laço de repetição
# para solicitar ao usuário as novas strings, chame a função e 
# imprima o resultado.
listaDePalavras = ["Abacaxi", "acerola", "uva", "kiwi", "caju",]
rodarWhile = True
rodarWhile1 = True

def cincoLetras(listaStrings):
    contador = 0
    for palavra in listaStrings:
        if len(palavra) > 5:
            contador += 1

    msg =f"Existe {contador} strings com mais de 5 caracteres."
    return msg

print(listaDePalavras)
print(cincoLetras(listaDePalavras))

print("\nDeseja adicionar mais strings a lista?")

while rodarWhile:
    
    continuarLista = input("Tecle [S]sim ou [N]não: ")
    if continuarLista in ["s","S","sim","Sim","n","N","não","Não","nao","Nao"]:
        if continuarLista in ["s","S","sim","Sim"]:
            while rodarWhile1:
                listaDePalavras.append(input("Insira a nova palavra: "))
                valorInput = input(f"\nAdicionar mais um item? Tecle [S]sim ou [N]não: ")
                if  valorInput in ["s","S","sim","Sim","n","N","não","Não","nao","Nao"]:
                    if valorInput in ["n","N","não","Não","nao","Nao"]:
                        rodarWhile1 = False
                        rodarWhile = False
                    else:
                        pass
                else:
                    print("comando inválido")

                rodarWhile1

        else:
            print("Obrigado por ter usado a nossa função")
            rodarWhile = False   
    else:
        print("comando inválido")


print(listaDePalavras)
print(cincoLetras(listaDePalavras))