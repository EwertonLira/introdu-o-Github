# 6 Escreva uma função que receba um número inteiro como parâmetro e retorne True se o número for primo e False 
# caso contrário. A função deve utilizar uma variável local para armazenar o resultado e uma estrutura de 
# repetição para verificar se o número é divisível por outro número. Em seguida, utilize uma variável global 
# para contar quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada chamada.

vezesFuncaoUtilizada = 0
rodarWhile = True
rodarWhile1 = True
rodarWhile2 = True

def isPrime(valor):
    global vezesFuncaoUtilizada
    vezesFuncaoUtilizada += 1

    primo = True
    for numero in range(2,valor):
        if valor % numero == 0:
            primo = False 
    
    if valor in [0,1]:
        primo = False
    

    msg = f"""
    {valor} is {primo}.
    A função foi utilizada {vezesFuncaoUtilizada} vezes.
    """
    return msg

while rodarWhile:
    
    while rodarWhile1: 
        try:
            numero = int(input("Insira um número para saber se ele é primo: "))
            print(isPrime(numero))
            rodarWhile1 = False
        except:
            print("somente número naturais")

        print("Deseja usar novamente a função?")
    
    while rodarWhile2:
            repetirScript = input("[S]sim ou [N]não: ") 
            if repetirScript in ["s","S","sim","Sim","n","N","não","Não","nao","Nao"]: # verifica se entrou um dado válido.
                rodarWhile2 = False
            else:
                print("digite sim ou não ou tecle [S] ou [N] e aperte ENTER")
                
    if repetirScript in ["s","S","sim","Sim"]: #caso o usuário queira usar novamente,deixamos os whiles True novamente.
        rodarWhile1 = True
        rodarWhile2 = True
    else:
        rodarWhile = False
    


                    
        
