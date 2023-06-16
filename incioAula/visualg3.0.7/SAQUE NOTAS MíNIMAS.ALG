Algoritmo "saque notas mínimas"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2023
Var
// Seção de Declarações das variáveis 
     saque,nota100,resto100,nota50,resto50,nota20,resto20:inteiro
      nota10,resto10,nota5,resto5,nota2,resto2,nota1,resto1:inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("digite o valor que deseja sacar:")
leia(saque)
nota100 <- int (saque / 100)
Resto100 <- (saque%100)
nota50 <- int (Resto100 / 50)
Resto50 <- (Resto100%50)
nota20 <- int (Resto50 / 20)
Resto20 <- (Resto50%20)
nota10 <- int (Resto20 / 10)
Resto10 <- (Resto20%10)
nota5 <- int (Resto10 / 5)
Resto5 <- (Resto10%5)
nota2 <- int (Resto5 / 2)
Resto2 <- (Resto5%2)
nota1 <- int (Resto2 / 1)
Resto1 <- (Resto2%1)
escreval("você receberá:")
se( nota100 <> 0) entao
escreval(nota100," notas de 100 reais")
fimse
se( nota50 <> 0) entao
escreval(nota50," notas de 50 reais")
fimse
se( nota20 <> 0) entao
escreval(nota20," notas de 20 reais")
fimse
se( nota10 <> 0) entao
escreval(nota10," notas de 10 reais")
fimse
se( nota5 <> 0) entao
escreval(nota5," notas de 5 reais")
fimse
se( nota2 <> 0) entao
escreval(nota2," notas de 2 reais")
fimse
se( nota1 <> 0) entao
escreval(nota1," notas de 1 reais")
fimse
Fimalgoritmo