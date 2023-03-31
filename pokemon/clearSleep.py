# from os import system, name 
# from time import sleep 
# def limparTela(): 
    
#     if name == 'nt': 
#         _ = system('cls') 
      
#     else: 
#         _ = system('clear') 

# print("kjsaljdjsjlkfj")

# input("kdjds")
# sleep(0.65) 
# limparTela()

import csv

arquivo = open('movePoke.csv')

pessoas = csv.reader(arquivo)

for pessoa in pessoas:
    print(pessoa)
