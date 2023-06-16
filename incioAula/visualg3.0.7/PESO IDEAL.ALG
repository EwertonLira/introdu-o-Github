Algoritmo "Peso ideal"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/02/2023
Var
// Seção de Declarações das variáveis 
      a, p :real
      s:caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
         Escreval("Digite o seu sexo com F ou M:")
            leia(s)
         Escreval("Digite a sua altura:")
            leia(a)
                  se(s = "f") então
               p <- (62.1 * a) - 44.7
         Escreval("Seu peso ideal é:",p)
                   senão
                  se(s = "m") então
                p <- (72.7 * a ) -  58
           Escreval("Seu peso ideal é:",p)
                         Senão
           Escreval("Digite um sexo válido")
                            fimse
                            fimse
                   
Fimalgoritmo