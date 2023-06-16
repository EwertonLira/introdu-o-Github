# testeListas 1

programadores = ['Victor','Juliana','Samuel','Caio','Luana']
print(type(programadores)) # type 'list'
print(len(programadores)) # 5
print(programadores[4]) #Luana

# testeListas 2
aluno = ['Murilo',19, 1.79] # Nome, idade e altura
print(type(aluno)) # type 'list'
print(aluno) # ['Murilo', 19, 1.79]


# testeListas 2 .split()
print(aluno[0].split("i"))
print(aluno[0].split("u"))

nome = input('Digite um nome')

if nome in programadores:
    print(nome,"está na lista")
else:
    print(nome, "não está na lista")

for programador in programadores:
    if nome == programador:
        print(nome, "está na lista")

for i in range(len(programadores)):

    if nome == programador[i]:
        print(nome,"está na lista, na posição", i)

