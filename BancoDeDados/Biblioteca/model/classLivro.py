
class Livros():
    def __init__(self): #nome, paginas, anoLancamento, autor, id = "default"):
        self._tipoClass = "livros"
        self._nomeTabela = "livro"
        self._id = None
        self._nome = None
        self._paginas = None
        self._anoLancamento = None
        self._autor = None

    def getTipoClass(self):
        return self._tipoClass
    
    def getNomeTabela(self):
        return self._nomeTabela

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

    def setInputDados(self):
        print("Insira os dados do livros nos campos abaixo:")

        self._nome = input("Insira o nome do livro")
        self._paginas = input("Insira o número de páginas do livro")
        self._anoLancamento = input("Insira o ano de lançamento do livro")
        self._autor = input("Insira o ID do autor")

    def consultarLivroPorID(self):
        sql = f'''
        SELECT * FROM "livros"
        WHERE "livro_id" = '{self._id}'
        '''
    def consultarLivro(self):
        sql = f'''
        SELECT * FROM "livros"
        ORDER BY "livro_id" ASC
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

    def criarTabela(self):
        sql = f'''
        CREATE TABLE "livros" (
        "livro_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "livro_nome" varchar(255) NOT NULL,
        "livro_paginas" varchar(255), NOT NULL DEFAULT 'não informado',
        "livro_ano_lancamento" varchar(255) NOT NULL DEFAULT 'não informado',
        "livro_autor" varchar(255) NOT NULL DEFAULT 'não informado',
        CONSTRAINT fk_autor
        FOREIGN KEY ("livro_autor")
        REFERENCES "autores"("autor_id")
        );
        '''
        return sql

