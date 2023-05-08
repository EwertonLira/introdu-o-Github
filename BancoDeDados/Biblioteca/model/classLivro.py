class Livros:
    def __init__(self, id, nome, paginas, anoLancamento, autor):
        self._tipoClass = "classLivro"
        self._id = id
        self._nome = nome
        self._paginas = paginas
        self._anoLancamento = anoLancamento
        self._autor = autor

    def getTipoClass(self):
        return self._tipoClass

    def getId(self):
        return self._id

    def getNome(self):
        return self._nome
    
    def getPaginas(self):
        return self._paginas
    
    def getAnoLancamento(self):
        return self._anoLancamento
    
    def getAutor(self):
        return self._autor

    def imprimirLivro(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        Número de páginas - {self._paginas}
        Ano de lançamento - {self._anoLancamento}
        Autor - {self._autor}
        ''')

    def consultarLivroPorID(self):
        sql = f'''
        SELECT * FROM "livros"
        WHERE "livro_id" = '{self._id}'
        '''
        
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "aluguel"
        WHERE "livro_id" = '{self._id}'
        '''
        
        return sql

    def cadastrarLivro(self):
        sql = f'''
        INSERT INTO "livros"
        VALUES(default, '{self._nome}', '{self._paginas}', '{self._anoLancamento}', '{self._autor}')
        '''

        return sql

livroTeste = Livros('default','as flores do meu jardim',45,1997,'chico Buarque')