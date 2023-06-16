
palavra = input('Insira uma palavra: ')
inverso = ""

for i in range(len(palavra)):
   inverso += palavra[len(palavra)-1-i]

print(inverso)

# for i in range(len(palavra)):

#    inverso += palavra[-(i+1)]

# print(inverso)   
 
#  print(palavra[::-1])

