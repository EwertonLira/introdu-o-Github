from classConexao import *
from customtkinter import *

conexaoBanco = Conexao()

app = CTk()
app.title("inserção de livro")

app.geometry("800x600")


tituloInserirLivro = CTkLabel(master=app,)
tituloInserirLivro.grid(column=0, row=1, padx=(20,50) ,pady=20)


rotuloNome = CTkLabel(master=app, text="Nome:")
rotuloNome.grid(column=0,row=1, padx=20,pady=20)

insercaoNome = CTkEntry(master=app, )
