class Aluguel:
    def __init__(self):
        self._id = None 
        self._idCliente = None
        self._idLivro = None
        self._dataRetirada = None
        self._dataEntrega = None
        self._notificacao = None
        self._status = "ativo"
    
    def setIdCliente(self, idCliente):
        self._idCliente = idCliente

    def setIdLivro(self, idLivro):
        self._idLivro = idLivro
    
    def _inputDadosAluguel(self):
        
        #self._idCliente = input("Insira o ID do cliente: ")
        #self._idLivro = input("Insira o ID do livro: ")
        self._dataRetirada = input("Insira a data de retirada: ")
        self._dataEntrega = input("Insira a data de entrega: ")
        self._notificacao = input("digite aqui alguma observação: ")

    def _imprimirAluguel(self):

        print(f'''
        ID do aluguel - {self._id}
        ID do Cliente  - {self._idCliente}
        ID do Livro  - {self._idLivro}
        Data de retirada - {self._dataRetirada}
        Data da Entrega - {self._dataEntrega}
        notificação - {self._notificacao}
        ''')

    def gerarListaAluguel(self):
            
            sql = f'''
            SELECT * FROM "aluguel"
            ORDER BY "aluguel_id" ASC
            '''
            return sql

    def verlistaAluguel(self,listaAluguel,TipoDeVisualizacao):
         # id aluguel [0]/ cliente ID[1]/ livro Id [2]/ retidada [3]/ entrega [4]/ observação [5] / status [6]
        
        match TipoDeVisualizacao:
            case "completa":
                for aluguel in listaAluguel:
                    if aluguel[6] == "ativo":
                        self._id = aluguel[0]
                        self._idCliente = aluguel[1]
                        self._idLivro = aluguel[2]
                        self._dataRetirada = aluguel[3]
                        self._dataEntrega = aluguel[4]
                        self._notificacao = aluguel[5]
                        
                        self._imprimirAluguel()
            
            case "id":
                print(" ID | Cliente | Livro")
                for aluguel in listaAluguel:
                    if aluguel[6] == "ativo":
                        self._id = aluguel[0]
                        self._idCliente = aluguel[1]
                        self._idLivro = aluguel[2]
                        print(f" {self._id}   {self._idCliente}  {self._idLivro}")

    def cadastrarAluguel(self):
        
        self._inputDadosAluguel()
        
        sql = f'''
        INSERT INTO "aluguel"
        VALUES(default, '{self._idCliente}', '{self._idLivro}', '{self._dataRetirada}', '{self._dataEntrega}', '{self._notificacao}', '{self._status}')
        '''
        return sql
    
    def atualizar(self, aluguelId):   
        opCampo = "rodarWhile"
        while not(opCampo in "1¬2¬3¬4¬5¬6¬0"):
            print('''
            qual campo deseja atualizar do aluguel?
            
            [1]📧 data de entrega
            [2]🎂 observações
            [0] ↩️ Voltar ao menu principal
            ''')
            opCampo = input(": ")
            match opCampo:
                case "1":
                    self._dataEntrega = input("Insira a nova data de entrega do aluguel: ")
                    sql = f'''
                        UPDATE "aluguel"
                        SET "aluguel_data_entrega" = '{self._dataEntrega}'
                        WHERE "aluguel_id" = '{aluguelId}';
                        '''
                case "2":
                    self._notificacao = input("Insira uma nova observação do  aluguel: ")
                    sql = f'''
                        UPDATE "aluguel"
                        SET "aluguel_notificacao" = '{self._notificacao}'
                        WHERE "aluguel_id" = '{aluguelId}';
                        '''
                case "0":
                    sql = None
                case _:
                    print("comando inválido Tente novamente")
                    input("aperte [Enter↵] para continuar")

            return sql
    
    def deletar(self, clienteID):
        sql = f'''
            UPDATE "aluguel"
            SET "aluguel_status" = 'desativado'
            WHERE "aluguel_id" = '{clienteID}';
            '''

        return sql