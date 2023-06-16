Algoritmo "Exercício 3"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/02/2023
Var
// Seção de Declarações das variáveis 
Salario, prestacao:real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
Escreval("Insira o valor do seu salário:")
    leia(salario)
Escreval("Insira o valor da prestação")
    leia(prestacao)
se prestacao > (0.2*salario) então
    escreval("Seu empréstimo foi negado")
                  senão
    escreval("seu empréstimo foi aprovado")
                  fimse
Fimalgoritmo