
def questão4():
    
    num1 = input('escreva o primeiro número inteiro: ')
    num2 = input('escreva o segundo número inteiro: ')
    num3 = input('escreva o terceiro número inteiro: ')

    primeiro = None
    segundo = None
    terceiro = None

    if (num1 != num2 and num1 != num3 and num2 != num3):
        if(num1 > num2 and num1 > num3):
            primeiro = num1
            if (num2 > num3):
                segundo = num2
                terceiro = num3
            else:
                segundo = num3
                terceiro = num2
        if(num2 > num1 and num2 > num3):
            primeiro = num2
            if (num1 > num3):
                segundo = num1
                terceiro = num3
            else:
                segundo = num3
                terceiro = num1
        if(num3 > num1 and num3 > num2):
            primeiro = num3
            if (num1 > num2):
                segundo = num1
                terceiro = num2
            else:
                segundo = num2
                terceiro = num1
    else:
     print('você não digitou 3 número diferentes')