Algoritmo "inverter números"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2023
Var
// Seção de Declarações das variáveis 
     numero,numero2,numero3:inteiro
     centena, dezena, unidade:inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("digite um número de três algarismos:")
leia(numero)

centena <- int (numero/100)

numero2 <- numero-(100* centena)
dezena <-  int (numero2/10)

numero3 <- numero2-(10*dezena)
unidade <-  int (numero3/1)

escreval("o número invertido é!")
escreval()
escreval(unidade,dezena,centena)

Fimalgoritmo