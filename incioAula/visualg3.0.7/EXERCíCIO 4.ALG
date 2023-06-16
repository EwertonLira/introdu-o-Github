Algoritmo "Exercício "
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/02/2023
Var
// Seçãfatoo de Declarações das variáveis
           fatorial6, fatorial5, fatorial4:real
           i:inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreval("fatorial de 6! é:",(raizq(1*2*3*4*5*6)),"²")
   escreval("fatorial de 5! é:",(raizq(1*2*3*4*5)),"²")
   escreval("fatorial de 4! é:",(raizq(1*2*3*4)),"²")

    fatorial6 <-1
    fatorial5 <-1
    fatorial4 <-1

    para i de 1 até 6 faça
    fatorial6 <- fatorial6 * i
    fimpara
    
    para i de 1 até 5 faça
    fatorial5 <- fatorial5 * i
    fimpara
    
    para i de 1 até 4 faça
    fatorial4 <- fatorial4 * i
    fimpara
    Escreval()
    escreval("fatorial de 6! é:",fatorial6)
    escreval("fatorial de 5! é:",fatorial5)
    escreval("fatorial de 4! é:",fatorial4)
Fimalgoritmo