
palavra = input('insira uma palavra: ')

impar = ""
for i in range(0,len(palavra),2):
    impar = impar + palavra[i]

print(f'as letras impares dessa palavras são : {impar}')