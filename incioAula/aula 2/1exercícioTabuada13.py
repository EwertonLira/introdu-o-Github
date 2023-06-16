#1exercícioTabuada13.py
#an=a1+(n-1)*r

a = int(input("insira o tamanho da tabuada do 13 que você deseja: "))
a = a + 1
for i in range(a):
    b = 13*i
    print(f'13 x {i} = {b}')
   
print("obrigado por usar a nossa tabuada!")

def questao1():
    for i in range(1,11):
        
        print(f'{i}. {i}x13 = {i*13}')

questao1()