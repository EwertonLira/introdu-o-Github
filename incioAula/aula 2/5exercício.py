
NomeAluno = input('insira o nome do aluno: ')
Nota1 = float(input(f'insira a 1ª nota do {NomeAluno}: '))
Nota2 = float(input(f'insira a 2ª nota do {NomeAluno}: '))
Nota3 = float(input(f'insira a 3ª nota do {NomeAluno}: '))

MediaAluno = (Nota1 + Nota2 + Nota3)/3

if MediaAluno >=7:
    print(f'O aluno {NomeAluno} foi aprovado com Média {MediaAluno}!')
elif MediaAluno <=5 :
    print(f'O aluno {NomeAluno} foi reprovado.')
elif MediaAluno<7 and MediaAluno>5:
    print(f'O aluno {NomeAluno} está de recuperação.')
else:
    print(f'invalido')
