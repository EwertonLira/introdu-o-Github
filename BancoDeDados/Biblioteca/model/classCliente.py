class Clientes:
    def __init__(self, id, nome, cpf, telefone, email, nascimento):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
        self._nascimento = nascimento
    
    def imprimirCliente(self):

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
        sql = f'''
        INSERT INTO "clientes"
        VALUES(default, '{self._nome}', '{self._cpf}', '{self._telefone}', '{self._email}', '{self._nascimento}')
        '''

        return sql