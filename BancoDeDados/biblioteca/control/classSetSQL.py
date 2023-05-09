
class SetSQL():
    def __init__(self, objSelecionado, comandoSQL, caminho = "model\comandos.sql" ):
        
        self._objSelecionado = objSelecionado
        self._comandoSQL = comandoSQL
        self._listaComandosSQL = ["select","selectid","insert","update","delete"]
            
        listaVerificacaoClass = ["model.classLivro.Livros","model.classAluguel.Aluguel","model.classCliente.Clientes"]
        classeDoObj = str(self._objSelecionado)
        classEncontrada = "nada"

        for itemClass in listaVerificacaoClass:
            if itemClass in classeDoObj:
                classEncontrada = itemClass
    
        print(classEncontrada)
        match classEncontrada:
            case "model.classLivro.Livros":
               self._verificadorObj = "livros"
            case "model.classAluguel.Aluguel":
               
            case "model.classCliente.Clientes":
                print("""Cliente
                        1. select
                        2. select ID
                        3. insert
                        4. update
                        5. delete""")
            case "nada":
                print("objeto não reconhecido")


        self._caminho = caminho
        self._verificadorObj = ""
        self._executar = ""
    
    def comandoEscolhidoSQL(self):
        with open(self._caminho, mode="r",newline="") as selectSQL:
            arquivoSql = selectSQL.read()
            listaInsertSql = arquivoSql.split("-- splitKeyComment "+self._executar)
            
            del listaInsertSql[0]
            del listaInsertSql[-1]


            for file in listaInsertSql:
                if self._verificadorObj in file:
                    resultado = file
            
        return resultado
    
    def verificarObj(self):
        
        listaVerificacaoClass = ["model.classLivro.Livros","model.classAluguel.Aluguel","model.classCliente.Clientes"]
        classeDoObj = str(self._objSelecionado)
        classEncontrada = "nada"

        for itemClass in listaVerificacaoClass:
            if itemClass in classeDoObj:
                classEncontrada = itemClass
    
        print(classEncontrada)
        match classEncontrada:
            case "model.classLivro.Livros":
               self._verificadorObj = "livros"
            case "model.classAluguel.Aluguel":
               
            case "model.classCliente.Clientes":
                print("""Cliente
                        1. select
                        2. select ID
                        3. insert
                        4. update
                        5. delete""")
            case "nada":
                print("objeto não reconhecido")

    def verificarExecutarComando(self):
        comando = self._comandoSQL.lower()

        for comandosSQL in self._listaComandosSQL: 
            if comando == comandosSQL:
                resultadoVerficacao = comando
                print(resultadoVerficacao)
                break
        else:
            print("comando SQL não encontrado, verifique os comandos no arquivo comandos SQL")
        
        match resultadoVerficacao:
            case "select":
                self._executar = "select"
                
                
            








    


    def modificarSQL(self,objSelecionado,comandoSQL,):
        with open(self._caminho, mode='r') as arquivo:
            # ler o conteúdo do arquivo
            conteudo = arquivo.read()

            # substituir a palavra "antiga" pela palavra "nova"
            novo_conteudo = conteudo.replace("{livroIDSelect}", dadoEscolhido)

        with open(self._caminho, mode='w') as arquivo:
            # escrever o conteúdo atualizado no arquivo
            arquivo.write(novo_conteudo)
