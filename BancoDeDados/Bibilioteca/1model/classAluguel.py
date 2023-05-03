class Aluguel:
    def __init__(self, id, idCliente, idLivro, dataRetirada, dataEntrega, notificacao):
        self._id = id 
        self._idCliente = idCliente
        self._idLivro = idLivro
        self._dataRetirada = dataRetirada
        self._dataEntrega = dataEntrega
        self._notificacao = notificacao
    
    def cadastrarAluguel(self):
        sql = f'''
        INSERT INTO "aluguel"
        VALUES(default, '{self._idCliente}', '{self._idLivro}', '{self._dataRetirada}', '{self._dataEntrega}', '{self._notificacao}')
        '''
        return sql
    