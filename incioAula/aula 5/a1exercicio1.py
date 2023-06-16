
nome = input('insira o seu nome: ')

numeroLetras = len(nome) - nome.count(" ")

print(f'''O número de letras do seu nome é {numeroLetras}
e começa com a letra: {nome[0]}''')

contadorletras = 0
for letra in nome:
    if letra != " ":
        contadorletras += 1