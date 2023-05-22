
class Clientes:
    def __init__(self):
        self._id = None
        self._nome = None
        self._cpf = None
        self._telefone = None
        self._email = None
        self._nascimento = None
        self._status = "ativo"
    
    def _setCPF(self,CPF):
        numeros = len(CPF)
        
        try:
           resultado =  int(CPF)
        except:
            resultado = False

        if (numeros == 11) and (resultado):
            self._cpf = CPF
            resultado = False
        else:
            print("o cpf deve ser 11 números, sem pontos ou traços")
            resultado = True
        
        return resultado

    def _inputDadosCliente(self):
        
        self._nome = input("Insira o nome do cliente: ")
        
        chave = True
        while chave:
            cpf = input("Insira o CPF: ")
            chave = self._setCPF(cpf)
        
        self._telefone = input("Insira o telefone: ")
        self._email = input("Insira um endereço eletrônico: ")
        self._nascimento = input("data de nascimento:  ")

        

    def _imprimirCliente(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CPF - {self._cpf}
        Telefone - {self._telefone}
        Email - {self._email}
        Data de nascimento - {self._nascimento}
        ''')

    def consultarClientePorID(self):
        sql = f'''
        SELECT * FROM "clientes"
        WHERE "cliente_id" = '{self._id}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "aluguel"
        WHERE "cliente_id" = '{self._id}'
        '''
        return sql

    def cadastrarCliente(self):
        print("Insira os dados do Cliente")
        self._inputDadosCliente()
        
        sql = f'''
        INSERT INTO "clientes"
        VALUES(default, '{self._nome}', '{self._cpf}', '{self._telefone}', '{self._email}', '{self._nascimento}', '{self._status}')
        '''

        return sql
    
    def gerarListaClientes(self):
        
        sql = f'''
        SELECT * FROM "clientes"
        ORDER BY "cliente_id" ASC
        '''
        return sql
    
    def verlistaClientes(self,listaClientes,TipoDeVisualizacao):
         # id cliente [0]/ nome[1]/ cpf [2]/ telefone[3]/ email [4]/ nascimento [5] / status [6]
        
        match TipoDeVisualizacao:
            case "completa":
                for cliente in listaClientes:
                    if cliente[6] == "ativo":
                        self._id = cliente[0]
                        self._nome = cliente[1]
                        self._cpf = cliente[2]
                        self._telefone = cliente[3]
                        self._email = cliente[4]
                        self._nascimento = cliente[5]
                        
                        self._imprimirCliente()
            
            case "id":
                print("\n ID | nome")
                for cliente in listaClientes:
                    if cliente[6] == "ativo":
                        self._id = cliente[0]
                        self._nome = cliente[1]
                        print(f" {self._id}   {self._nome}")
    
    def atualizar(self, clienteID):   
        opCampo = "rodarWhile"
        while not(opCampo in "1¬2¬3¬4¬5¬6¬0"):
            print('''
            qual campo deseja atualizar do Cliente?
            
            [1]🔤 Nome
            [2]💳 CPF
            [3] 📱 telefone
            [4]📧 email
            [5]🎂 Data de nascimento
            [6] Todos os campos
            [0] ↩️ Voltar ao menu principal
            ''')
            opCampo = input(": ")
            match opCampo:
                case "1":
                    self._nome = input("Insira o novo nome do cliente: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_nome" = '{self._nome}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "2":
                    self._cpf = input("Insira o novo CPF do cliente: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_cpf" = '{self._cpf}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "3":
                    self._telefone = input("Insira o novo telefone do Cliente: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_telefone" = '{self._telefone}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "4":
                    self._email = input("Insira o novo email do cliente: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_email" = '{self._email}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "5":
                    self._nascimento = input("Insira a quantidade do produto: ")
                    sql = f'''
                        UPDATE "clientes"
                        SET "cliente_nascimento" = '{self._nascimento}'
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "6":
                    self._inputDadosCliente()
                    sql = f''' UPDATE "clientes"
                        SET "cliente_nome" = '{self._nome}',
                            "cliente_cpf" = '{self._cpf}',
                            "cliente_telefone" = '{self._telefone}',
                            "cliente_email" = '{self._email}',
                            "cliente_nascimento" = '{self._nascimento}'    
                        WHERE "cliente_id" = '{clienteID}';
                        '''
                case "0":
                    sql = None
                case _:
                    print("comando inválido Tente novamente")
                    input("aperte [Enter↵] para continuar")

            return sql
    
    def deletar(self, clienteID):
        sql = f'''
            UPDATE "clientes"
            SET "cliente_status" = 'desativado'
            WHERE "cliente_id" = '{clienteID}';
            '''

        return sql