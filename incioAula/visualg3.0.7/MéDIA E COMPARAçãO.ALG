Algoritmo "média e comparação"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/02/2023
Var
// Seção de Declarações das variáveis 
            notas: vetor [1..5] de inteiro
            i, maior_media, soma:inteiro
            media: real
            
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
Escreval("Digite as 5 notas:")
          para i de 1 até 5 faça
          escreval("digite a",i,"ª nota")
          leia (notas[i])
     soma<- soma + notas[i]
     media<- soma/5
             fimpara
escreval("A soma das notas é:",soma)
escreval("A media das notas é:",media)
escreval("Os valores maiores que a média são:")

para i de 1 até 5 faça
se(notas[i] > media)entao
maior_media<-notas[i]
escreval(maior_media)
fimse
fimpara





Fimalgoritmo