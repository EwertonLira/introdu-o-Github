from customtkinter import *

app = CTk()
app.title("chat fake")

larguraJanela = 800
alturaJanela = 600
app.geometry(f"{larguraJanela}x{alturaJanela}")
app.grid_columnconfigure((0,1,2), weight=1)
app.grid_rowconfigure((0,1,2), weight=1)


def inserirTextoNaCaixa(*args, **kwargs):

    texto = inserirTexto.get()

    resultado = f"{texto}\n"

    telachat.configure(state = "normal")

    telachat.insert("end",resultado)

    telachat.configure(state = "disabled")

    telachat.delete(0,"end")


tituloTopo = CTkLabel (master=app, text = "chat fake", text_color = "blue",font=CTkFont(size=36,weight="normal"))
tituloTopo.grid(row=0,column=1, padx=20,pady=20, stick="nsew")

widgetEnvioMensagem = CTkFrame(master=app,fg_color="#a5c4e0")
widgetEnvioMensagem.grid(column=1, row=2, padx= 30,pady=(0,30),stick="ew")
widgetEnvioMensagem.columnconfigure(0, weight=1)

telachat = CTkTextbox (master=app,bg_color="gray",border_color="blue",scrollbar_button_color="purple",text_color="yellow")
telachat.grid(row=1, column=1, padx=20, pady=20, stick="nsew")


inserirTexto = CTkEntry(master=widgetEnvioMensagem, placeholder_text="Digite uma nova mensagem aqui!")
inserirTexto.grid(row=0, column=0, padx=20, pady=20,sticky="nsew")

inserirBotao= CTkButton(master = widgetEnvioMensagem, bg_color="blue", text="Enviar", command=inserirTextoNaCaixa())
inserirBotao.grid(row=0,column=1, padx=20, pady=20, sticky="nsew")
inserirBotao.place()

app.mainloop()