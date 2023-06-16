#ExercícioDicionario.py

aluno = {"nome": 'Ewerton',"ultimoNome":'Lira',"idade":28,"curso":'Senac',"endereço":'Caucaia'}

# print("a)")
print(aluno.items())
# print("b)")
print(aluno["nome"])
print(aluno["ultimoNome"])
print(aluno["idade"])
print(aluno["curso"])
print(aluno["endereço"])
# print("c)")
del aluno["curso"]
# print("d)")
aluno["ultimoNome"] = 'Lopes'
# print("e)")
print(aluno.items())
# print("f)")
print(aluno["endereço"])
# print("g)")
aluno2 = aluno.copy()
aluno2["nome"] = "Miguel"
aluno2["idade"] = 5
# print("h)")
print(aluno2.items())
