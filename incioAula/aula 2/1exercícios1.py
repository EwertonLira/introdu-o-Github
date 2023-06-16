
def questaoLanchonete():

    print('''
    
    Especificação Preço unitário
    100 Cachorro quente 1,10
    101 Bauru simples 1,30
    102 Bauru c/ovo 1,50
    103 Hamburger 1,10
    104 Cheeseburger 1,30
    105 Refrigerante 1,00
    
    
    ''')
    
    codigo = 0
    while codigo <= 99 or codigo >= 106:
        codigo = (input("Insira o código do produto escolhido: "))
    
    quantidade = input("Quantos deseja comprar: ")
            
    preco = 0
    nome = ""

    if codigo == 100 :
        nome = "Cachorro Quente"
        preco = 1.10
    elif codigo == 101 :
        nome = "Bauru Simples"
        preco = 1.30
    elif codigo == 102 :
        nome = "Bauru c/ ovo"
        preco = 1.50
    elif codigo == 103 :
        nome = "Hamburguer"
        preco = 1.10
    elif codigo == 104 :
        nome = "Cheeseburguer"
        preco = 1.30
    elif codigo == 105 :
        nome = "Refrigerante"
        preco = 1.00

    valorTotal = preco * quantidade
    print(f"Você comprou {quantidade} {nome} por R$ {valorTotal}")

    # match codigo:
    #     case "100":
    #         nome = "Cachorro Quente"
    #         preco = 1.10
    #     case "101":
    #         nome = "Bauru Simples"
    #         preco = 1.30
    #     case "102":
    #         nome = "Bauru c/ ovo"
    #         preco = 1.50
    #     case "103":
    #         nome = "Hamburguer"
    #         preco = 1.10
    #     case "104":
    #         nome = "Cheeseburguer"
    #         preco = 1.30
    #     case "105":
    #         nome = "Refrigerante"
    #         preco = 1.00


questaoLanchonete()
