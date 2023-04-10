import json
caminho = "modelagemArmazenamentoDeDados/Aula01.json"

def abrirArquivo():
    with open(caminho, "r") as arquivoJson:
        lista = json.load(arquivoJson)
        dic = lista["funcionarios"][0]
        for elemento in dic:
            print(elemento)
            
            # print(funcionário["id_funcionario"])
            # print(funcionário["id_nome"])
            # print(funcionário["id_cpf"])
            # print(funcionário["id_departamento"])

abrirArquivo()