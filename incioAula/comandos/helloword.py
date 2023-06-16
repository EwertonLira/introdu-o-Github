#helloword.py
'''as paspas triplas são 
comentários em mais de uma
linha'''
# w3 scholl site
msg = "hello word"
print("")
   
def hello():
    print(msg)
    print("não esqueça as aspas") 

print()
print(msg.upper()) #  .upper() deixa as letras maiúsculas.

print("!")
print("!")

hello()
hello()

msg1 = "hello"
msg2 = "word"
msg3 = "Ewerton"
print()
print(msg1,msg2,msg3)
print(msg1+" "+msg2+" "+msg3)
print(f"{msg1} {msg2} {msg3}")  #recomdendada
print("{} {} {}".format(msg1,msg2,msg3))


nome = input("escreva o seu nome:->")
print(f"olá {nome} seja bem vindo!")
print(f"{nome}")


nome2 = input ("escreva o seu nome: ")
print("A primeira letra do seu Nome é "+nome2[0].upper())
print()