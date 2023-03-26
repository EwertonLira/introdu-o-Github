# 5 Escreva uma função que receba uma lista de strings como parâmetro e retorne a string com o maior número de 
# caracteres. A função deve utilizar uma variável local para armazenar a string com o maior número de caracteres
# e uma estrutura de repetição para percorrer a lista. Em seguida, utilize uma variável global para contar
# quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada chamada.
palavras = ["banana","abacate","acerola","goiaba","kiwi","caju","uva","ameixa","maça","pêra"]
palavras1 = ["calça","bermuda", "short", "saia", "camiseta"]
palavras2 = ["Salvador Dalí","michelangelo","leonardo da vinci","donatello","rafael sanzio","Pierre-Auguste Renoir"]
vezesFuncaoUtilizada = 0

def maiorString(listaString):
    
    global vezesFuncaoUtilizada
    vezesFuncaoUtilizada += 1
    
    maiorPalavra = ""
    
    for palavra in listaString:
        
        if len(maiorPalavra) < len(palavra):
            maiorPalavra = palavra

    msg = f"""
    A maior palavra da lista é: {maiorPalavra}.
    A função foi utilizada {vezesFuncaoUtilizada} vezes.
    """
    return msg

print(maiorString(palavras))
print(maiorString(palavras1))
print(maiorString(palavras2))

