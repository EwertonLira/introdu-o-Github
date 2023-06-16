nome = ['abacate', 'acerola', 'maçã','uva', 'goiaba']

for a in nome:
    print(a)

print('______________________________________')

print(nome[0:2])

print('______________________________________')

for a in nome[3]:
    print(a)

print('______________________________________')

for i in range(5):
    print(nome[i])

print('______________________________________')

cpfvalido = True

while cpfvalido == True:
    cpf = input("insira o seu CPF")
    if len(cpf) != 11:
        print("o CPF deve ter 11 digitos.")
    else:
        print('obrigado!')
        break

    
print('______________________________________')    

