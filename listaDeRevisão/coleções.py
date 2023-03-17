# Coleções

# 1. Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.

# 2. Escreva um programa que leia uma lista de nomes e crie um dicionário onde 
# a chave é o nome e o valor é o número de vezes que o nome aparece na lista.

# 3. Escreva um programa que leia uma lista de números inteiros e remova todos os valores duplicados.
# Em seguida, imprima a lista sem os valores duplicados.

def questão1():
    MinhaLista = []
    
    print("Insira 5 números inteiros: ")
    for item in range(5):
        MinhaLista.append(int(input(f"Insira o {item + 1} número: da lista: "))) # vai inserir o número direto na lista. O valor de {item} começará por zero por isso + 1
    
    print(f"\nO menor número dessa lista é {min(MinhaLista)}.\nO maior é {max(MinhaLista)}.\n")

def questão2():
    
    listaNomes = []
    dicionariosNomes = {}
    
    print("Insira 5 nomes em uma lista: ") # cabeçalho da lista que vai ser pedida
    
    for repetições in range(6): # vai pedir 6 nomes e inserir na lista
       listaNomes.append(input(f"Insira o {repetições + 1}º nome da lista: ").lower()) # vai adicionar um nome por vez na lista com as letras todas minúsculas .lower()
   
    listaNomesConjunto = set(listaNomes) # transfomou a lista em conjunto para tirar os nomes repetidos
    listaNomeUnicos = list(listaNomesConjunto) # trasformou o conjunto em lista novamente. fiz isso porque não consegue fazer os comandos funcionar em .set
    
    for nome in listaNomeUnicos: # vai pegar cada nome da lista já filtrada de nomes.
        contagemDoNome = listaNomes.count(nome) # vai contar quantas vezes o nome da pessoa aparece na lista.
        dicionariosNomes[nome] = contagemDoNome # vai adicionar ao dicionário a chave com o nome da pessoa e o valor o resultado da contagem.

    print(dicionariosNomes) 

def questão3():
    listaNumero = []
    portaLógica = True
    print("Insira números inteiros e aperter [S] para confirmar ou [N] para Cancelar")
    while portaLógica :
        valorDeEntrada = input("Insira um número inteiro ou tecle [S]/[N]: ")
        
        contador = 0
        for letra in valorDeEntrada:
            if letra in ["0","1","2","3","4","5","6","7","8","9"]:
                contador += 1
        
        if contador == len(valorDeEntrada):
            listaNumero.append(int(valorDeEntrada))
        elif valorDeEntrada in ["s","S"]:
            portaLógica = False
        elif valorDeEntrada in ["n","N"]:
            listaNumero.clear()
            portaLógica = False
            print("[]")
            print("fim da aplicação")
        else:
            print("Insira um número inteiro ou tecle [S]/[N]: Continue apenas números inteiros ou [S] ou [N]")
    
    print(listaNumero)

questão3()