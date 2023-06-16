Algoritmo "exercício8"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/02/2023
Var
// Seção de Declarações das variáveis 
          na, nb, nc:real
          maiorNAnb, MaiorNanbEnc:real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
Escreval("insira primeiro número")
leia(na)
Escreval("insira segundo número")
leia(nb)
Escreval("insira o último número")
leia(nc)
   se (na > nb)então
   maiorNanb <- na
   senão
   maiorNanb <- nb
   fimse
   se(maiorNanb > nc)então
    MaiorNanbEnc <- maiorNanb
    senão
      MaiorNanbEnc <- nc
    fimse

Escreval("o número",MaiorNanbEnc," é o maior")


Fimalgoritmo