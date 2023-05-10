from customtkinter import *

app = CTk()
app.title("Sistema XYZ")

larguraJanela = 720
alturaJanela = 1280
app.geometry(f"{larguraJanela}x{alturaJanela}")
app.grid_columnconfigure((0,1,2), weight=1)
app.grid_rowconfigure((0,1), weight=1)

def cliqueInserir():
    texto = inserirTexto.get()
    corpoDoTexto.configure(text=texto)



tituloTopo = CTkLabel (master=app, text = "olá mundo", text_color = "blue",font=CTkFont(size=36,weight="normal"))
tituloTopo.grid(row=0,column=1, padx=20,pady=20)

corpoDoTexto = CTkLabel(master = app, text="este é meu programa!", text_color = "black",bg_color="white",font=CTkFont(size=16))
corpoDoTexto.grid(row=1, column=1, padx=20,pady=20)

inserirTexto = CTkEntry(master=app, placeholder_text="Digite uma nova mensagem aqui!")
inserirTexto.grid(row=2, column=1, padx=20, pady=20)

inserirBotao= CTkButton(master = app, bg_color="blue", text="Enviar", command=cliqueInserir)
inserirBotao.grid(row=2,column=0, padx=20, pady=20, sticky="n")
inserirBotao.place()

app.mainloop()