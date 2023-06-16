#IfElifElse.py
idade = int(input("digite a sua idade"))
if idade >=10 and idade < 20:
    print('Você é adolescente')
elif idade >=20 and idade < 30:
    print('você é jovem')
elif idade >= 30 and idade <= 100:
    print('você é adulto')
else:
    print('valor não encontrado!')



if idade == 10:
    print('sua idade é 10')
else: 
    if idade == 11:
        print("sua idade é 11")
    else:
        print("não é 10 nem 11")
