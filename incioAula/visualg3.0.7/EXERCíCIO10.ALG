Algoritmo "Exerc�cio10"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/02/2023
Var
// Se��o de Declara��es das vari�veis 
            num1, num2,maior,menor:real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Insira o primeiro n�mero:")
leia(num1)
escreval("Insira o segundo n�mero:")
leia(num2)
se(num1 = num2)ent�o
escreval("os n�meros s�o iguais!")
sen�o
se (num1 > num2)ent�o
maior <- num1
menor <- num2
escreval("O n�mero:",maior," � o maior")
escreval("O n�mero:",menor," � o menor")
sen�o
maior <- num2
menor <- num1
escreval("O n�mero:",maior," � o maior")
escreval("O n�mero:",menor," � o menor")
fimse
fimse


Fimalgoritmo