# Coleções

# 1. Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.

# 2. Escreva um programa que leia uma lista de nomes e crie um dicionário onde a chave é o nome e o valor é o número de
# vezes que o nome aparece na lista.

# 3. Escreva um programa que leia uma lista de números inteiros e remova todos os valores duplicados. Em seguida, imprima a lista sem os valores duplicados.

def questão1():
    MinhaLista = []
    
    print("Insira 5 números inteiros: ")
    for item in range(5):
        MinhaLista.append(int(input(f"Insira o {item + 1} número: da lista: "))) # vai inserir o número direto na lista. O valor de {item} começará por zero por isso + 1
    
    print(f"\nO menor número dessa lista é {min(MinhaLista)}.\nO maior é {max(MinhaLista)}.\n")

def questão2():
    listaNomes = []
    dicionariosNomes = {}
    listaAuxiliar = []

    print("Insira 5 nomes em uma lista: ")
    
    for repetições in range(6): # vai pedir 6 nomes
       listaNomes.append(input(f"Insira o {repetições + 1}º nome da lista: ").lower()) # vai adicionar um nome por vez na lista com as letras todas minúsculas .lower()

    # O primeiro for server para buscar na lista o item que vou pesquisar
    # O segundo for server para buscar todos os itens da lista para comparar com o que eu quero:
     
    for itemProcurado in range((len(listaNomes))):
        print(itemProcurado)
        contador = 0  
        for posDosItensPesquisados in range(len(listaNomes)):
            print(posDosItensPesquisados)
            if listaNomes[itemProcurado] in listaNomes[posDosItensPesquisados]: # and (posDosItensPesquisados) <= len(listaNomes):
                contador += 1
                listaAuxiliar.append((listaNomes[itemProcurado]+str(contador)))

    print(listaAuxiliar)
    print(listaNomes)



    
    


questão2()