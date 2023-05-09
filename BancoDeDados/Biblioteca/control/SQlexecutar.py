caminho = "model\comandos.sql"
comandoSQL = "selectID"

def executarSQL(obj, caminho,comandoSQL,variávelID = None):
    match comandoSQL:
        case 'selectID':
            nomeAntigo = "{livroIDSelect}"
            nomeNovo = variávelID
            splitKey = "-- splitKeyComment select ID"
            tipoClass = obj.getTipoClass()


    with open(caminho, mode='r') as arquivo:
        # ler o conteúdo do arquivo
        conteudo = arquivo.read()

        # substituir a palavra "antiga" pela palavra "nova"
        novo_conteudo = conteudo.replace(nomeAntigo, nomeNovo)

    with open(caminho, mode='w') as arquivo:
        # escrever o conteúdo atualizado no arquivo
        arquivo.write(novo_conteudo)
    
       
    # with open(caminho, mode="r",newline="") as fileInsertSql:
    #     arquivoSql = fileInsertSql.read()
    #     listaInsertSql = arquivoSql.split(splitKey)
        
    #     del listaInsertSql[0]
    #     del listaInsertSql[-1]

    #     for file in listaInsertSql:
    #         if tipoClass in file:
    #             print(file)
    #             sql = file
            
    # with open(caminho, mode='r') as arquivo:
    # # ler o conteúdo do arquivo
    #     conteudo = arquivo.read()

    #     # substituir a palavra "antiga" pela palavra "nova"
    #     novo_conteudo = conteudo.replace(nomeNovo, nomeAntigo)

    # with open(caminho, mode='w') as arquivo:
    #     # escrever o conteúdo atualizado no arquivo
    #     arquivo.write(novo_conteudo)
    
    # return 