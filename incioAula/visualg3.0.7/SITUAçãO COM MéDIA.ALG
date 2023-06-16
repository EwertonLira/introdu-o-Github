Algoritmo "Situação com média"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/02/2023
Var
// Seção de Declarações das variáveis 
            n1,n2,n3,n4,media:real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
             Escreval("Digite a 1ª nota:")
               leia(n1)
             Escreval("Digite a 2ª nota:")
               leia(n2)
             Escreval("Digite a 3ª nota:")
               leia(n3)
             Escreval("Digite a 4ª nota:")
               leia(n4)
              media <- (n1+n2+n3+n4)/4
                      se(media >=5)então
                Escreval("O aluno foi aprovado com média:",media)
                      senão
                 Escreval("O aluno não foi aprovado com média:",media)
                             fimse
              
              
              
Fimalgoritmo