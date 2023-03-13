# Coleções

# 1. Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.

# 2. Escreva um programa que leia uma lista de nomes e crie um dicionário onde a chave é o nome e o valor é o número de vezes que o nome aparece na lista.

# 3. Escreva um programa que leia uma lista de números inteiros e remova todos os valores duplicados. Em seguida, imprima a lista sem os valores duplicados.

def questão1():
    MinhaLista = []
    
    print("Insira 5 números inteiros: ")
    for item in range(5):
        MinhaLista.append(int(input(f"Insira o {item + 1} número: da lista: "))) # vai inserir o número direto na lista. O valor de {item} começará por zero por isso + 1
    
    print(f"\nO menor número dessa lista é {min(MinhaLista)}.\nO maior é {max(MinhaLista)}.\n")

def questão2():
    