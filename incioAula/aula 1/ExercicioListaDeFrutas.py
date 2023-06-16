# ExercicioListaDeCompras

a = input("digite o nome da 1º fruta: ")
b = input("digite o nome da 2º fruta: ")
c = input("digite o nome da 3º fruta: ")
d = input("digite o nome da 4º fruta: ")
e = input("digite o nome da 5º fruta: ")
preco = 1
print("A fruta", a,"Custa R$", preco)
print("A fruta", b,"Custa R$", preco*2)
preco = preco/2 # a partir daqui a variável preço deixa de ser 1 passa a valer 1/2 que é igual a 0,5
print("A fruta", c,"Custa R$", preco)
preco = preco*3 # a partir daqui a variável 0,5 passa a valer 0,5*3 que é igual a 1.5
print("A fruta", d,"Custa R$", preco)
print("A fruta", e,"Custa R$", preco/2)
