"""
1 Escreva uma função que receba uma lista de números inteiros e retorne o maior número da lista.
2 Escreva uma função que receba uma lista de palavras e retorne uma lista contendo apenas as palavras que começam com a letra "a".
3 Escreva uma função que receba uma lista de números inteiros e retorne a soma dos números pares da lista.
4 Escreva uma função que receba uma lista de dicionários contendo informações sobre pessoas (nome, idade, cidade) e retorne uma lista contendo apenas os nomes das pessoas que moram em uma cidade específica.
"""

numerosInteiros = [100,105,200,205,300,305,400,405,500,15,20,35,40,50,65,70,85,95,90,120,125]
palavras = ["banana","abacate","acerola","goiaba","kiwi","caju","uva","ameixa","maça","pêra"]
endereco = [
    {"nome":"Paulo", "idade":62, "cidade":"tarso"},
    {"nome":"Ewerton", "idade":28, "cidade":"caucaia"},
    {"nome":"Jesus", "idade":33, "cidade":"nazaré"},
    {"nome":"Tom hanks", "idade":60, "cidade":"oakland"},
    {"nome":"Hedy Lamarr", "idade":85, "cidade":"viena"},
    {"nome":"Miguel", "idade":5, "cidade":"caucaia"},
    {"nome":"Rafael", "idade":3, "cidade":"caucaia"}
    ]

def maiorNumero(lista):
    msg = f"O maior número da lista é: {max(lista)}"
    return msg

def retornarPalavrasA(lista):
    listaLetraA = []
    for cadaPalavra in lista:
        if cadaPalavra[0] in ["a","A"]:
            listaLetraA.append(cadaPalavra)
    msg = f"As palsvras que começam com a letra [A] são:\n{listaLetraA}"
    return msg

def somaNumerosPares(lista):
    totalSomaPares = 0
    for cadaNumeroDalista in lista:
        if cadaNumeroDalista % 2 == 0:
            totalSomaPares = totalSomaPares +cadaNumeroDalista
    
    msg = f"A soma de todos os números pares da lista é: {totalSomaPares}"
    return msg

def moradorCidade(lista,cidadeProcurada):
    str(cidadeProcurada).lower
    listaMoradoresCidade = []
    for nomeIdadeCidade in lista:
        if cidadeProcurada == nomeIdadeCidade["cidade"]:
            listaMoradoresCidade.append(nomeIdadeCidade["nome"])
    
    msg = f"Moradores de {cidadeProcurada.capitalize()}:\n{listaMoradoresCidade}"
    return msg

print(f"""
{maiorNumero(numerosInteiros)}

{retornarPalavrasA(palavras)}

{somaNumerosPares(numerosInteiros)}

{moradorCidade(endereco,"caucaia")}
""")