Algoritmo "m�dia e compara��o"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/02/2023
Var
// Se��o de Declara��es das vari�veis 
            notas: vetor [1..5] de inteiro
            i, maior_media, soma:inteiro
            media: real
            
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
Escreval("Digite as 5 notas:")
          para i de 1 at� 5 fa�a
          escreval("digite a",i,"� nota")
          leia (notas[i])
     soma<- soma + notas[i]
     media<- soma/5
             fimpara
escreval("A soma das notas �:",soma)
escreval("A media das notas �:",media)
escreval("Os valores maiores que a m�dia s�o:")

para i de 1 at� 5 fa�a
se(notas[i] > media)entao
maior_media<-notas[i]
escreval(maior_media)
fimse
fimpara





Fimalgoritmo