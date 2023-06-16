Algoritmo "Exercício10"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/02/2023
Var
// Seção de Declarações das variáveis 
            num1, num2,maior,menor:real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Insira o primeiro número:")
leia(num1)
escreval("Insira o segundo número:")
leia(num2)
se(num1 = num2)então
escreval("os números são iguais!")
senão
se (num1 > num2)então
maior <- num1
menor <- num2
escreval("O número:",maior," é o maior")
escreval("O número:",menor," é o menor")
senão
maior <- num2
menor <- num1
escreval("O número:",maior," é o maior")
escreval("O número:",menor," é o menor")
fimse
fimse


Fimalgoritmo