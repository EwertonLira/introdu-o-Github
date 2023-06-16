def contarString(nome,letra):
    contador = 0
    for i in nome:
        if i == letra:
            contador += 1
    
    return contador

nome = input("Insira a palavra: ")
letra = input("insira a letra a ser contada: ")

resultado = contarString(nome,letra)

print(f"A letra {letra} aparece {resultado} vezes na palavra \n{nome}")



# def contarLetras(palavra,letra):
#     contador = 0
#     for l in palavra:
#         if l.lower() == letra.lower():
#             contador +=1
    
#     return contador

# pal = input("Digite uma palavra: ")
# let = input("Digite uma letra: ")

# contagem = contarLetras(pal,let)

# print(f"A letra {let} aparece {contagem} vezes na palavra \n{pal}")
