Algoritmo "Situa��o com m�dia"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/02/2023
Var
// Se��o de Declara��es das vari�veis 
            n1,n2,n3,n4,media:real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
             Escreval("Digite a 1� nota:")
               leia(n1)
             Escreval("Digite a 2� nota:")
               leia(n2)
             Escreval("Digite a 3� nota:")
               leia(n3)
             Escreval("Digite a 4� nota:")
               leia(n4)
              media <- (n1+n2+n3+n4)/4
                      se(media >=5)ent�o
                Escreval("O aluno foi aprovado com m�dia:",media)
                      sen�o
                 Escreval("O aluno n�o foi aprovado com m�dia:",media)
                             fimse
              
              
              
Fimalgoritmo