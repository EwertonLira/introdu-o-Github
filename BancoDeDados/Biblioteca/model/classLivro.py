class Livros():
    def __init__(self):
        self._id = None
        self._nome = None
        self._paginas = None
        self._anoLancamento = None
        self._idAutor = None
        self._nomeAutor = None
        self._status = "ativo"


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

    def _imprimirLivro(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        páginas - {self._paginas}
        Ano de lançamento - {self._anoLancamento}
        Autor do livro - {self._nomeAutor}
        ''')

    def _setInputDados(self):

        self._nome = input("Insira o nome do livro: ")
        self._paginas = input("Insira o número de páginas do livro: ")
        self._anoLancamento = input("Insira o ano de lançamento do livro: ")
        self._nomeAutor = input("Insira o nome do autor: ")

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
        print("Insira os dados do Livro")
        self._setInputDados()
        
    def sqlCadastrarLivro(self):
        sql = f'''        ;
        INSERT INTO "livros"
        VALUES(default, '{self._nome}', '{self._paginas}', '{self._anoLancamento}', '{self._idAutor}', '{self._status}')
        '''
        return sql
    
    def gerarListalivros(self):
        sql = f'''
            SELECT * FROM "livros"
            ORDER BY "livro_id" ASC
            '''
        return sql

    def verlistaLivro(self,bancoDB,listaLivro,TipoDeVisualizacao):
         # id livro [0]/ nome[1]/ páginas [2]/ ano lançamento[3]/ autor ID [4]
        

        match TipoDeVisualizacao:
            case "completa":
                for livro in listaLivro:
                     if livro[5] == "ativo":
                        self._id = livro[0]
                        self._nome = livro[1]
                        self._paginas = livro[2]
                        self._anoLancamento = livro[3]
                        
                        #id autor [0] / nome autor [1]
                        listaAutor = bancoDB.consultarBanco(f'''
                        Select * from "autores"
                        where "autor_id" = '{livro[4]}'
                        ''')
                        self._nomeAutor = listaAutor[0][1]

                        self._imprimirLivro()
            
            case "id":
                print("\nID | Livro")
                for livro in listaLivro:
                    if livro[5] == "ativo":
                        self._id = livro[0]
                        self._nome = livro[1]
                        print(f" {self._id}   {self._nome}")

    def mudarStatusLivroAlugado(self,livroID):
        sql = f'''
                    UPDATE "livros"
                    SET "livro_status" = 'alugado'
                    WHERE "livro_id" = '{livroID}';
                    '''

        return sql

    def atualizar(self, livroID):   
        opCampo = "rodarWhile"
        while not(opCampo in "1¬2¬3¬4¬5¬0"):
            print('''
            qual campo deseja atualizar do livro?
                    
            [1]🔤 Nome
            [2]🔖 páginas
            [3]📅 ano de lançamento
            [4]✒️ autor do livro
            [5] Todos os campos
            [0] ↩️ Voltar ao menu principal
            ''')
            opCampo = input(": ")
            match opCampo:
                case "1":
                    self._nome = input("Insira o novo nome do livro: ")
                    sql = f'''
                        UPDATE "livros"
                        SET "livro_nome" = '{self._nome}'
                        WHERE "livro_id" = '{livroID}';
                        '''
                case "2":
                    self._paginas = input("Insira o novo numero de páginas do livro: ")
                    sql = f'''
                        UPDATE "livros"
                        SET "livro_paginas" = '{self._paginas}'
                        WHERE "livro_id" = '{livroID}';
                        '''
                case "3":
                    self._anoLancamento = input("Insira o novo ano de lançamento do livro: ")
                    sql = f'''
                        UPDATE "livros"
                        SET "livro_ano_lancamento" = '{self._anoLancamento}'
                        WHERE "livro_id" = '{livroID}';
                        '''
                case "4":
                    self._nomeAutor = input("Insira o novo nome do Autor do livro: ")
                    sql = f'''
                        UPDATE "autores"
                        SET "autor_nome" = '{self._nomeAutor}'
                        WHERE "autor_id" = '{livroID}';
                        '''
                case "5":
                    self._setInputDados()
                    sql = f''' UPDATE "livros"
                        SET "livro_nome" = '{self._nome}',
                            "livro_paginas" = '{self._paginas}',
                            "livro_ano_lancamento" = '{self._anoLancamento}'
                        WHERE "livro_id" = '{livroID}';

                        UPDATE "autores"
                        SET "autor_nome" = '{self._nomeAutor}'
                        WHERE "autor_id" = '{livroID}';

                        '''
                case "0":
                    sql = None
                case _:
                    print("comando inválido Tente novamente")
                    input("aperte [Enter↵] para continuar")

            return sql
    
    def deletar(self, livroID):
        sql = f'''
            UPDATE "livros"
            SET "livro_status" = 'desativado'
            WHERE "livro_id" = '{livroID}';
            '''

        return sql

    # ______________________________ Autor _____________________________
    # __________________________________________________________________
    def getIdAutor(self):
        return self._idAutor
    
    def getNomeAutor(self):
        return self._nomeAutor
    
    def setIdAutor(self, lista):
        for autor in lista:
            ultimoID = autor[0]

        self._idAutor = ultimoID
    
    def setNomeAutor(self, nome):
        self._nomeAutor = nome

    def cadastrarAutor(self):

        sql = f'''
        INSERT INTO "autores"
        VALUES(default, '{self._nomeAutor}')
        '''
        return sql
    
    def gerarListaAutor(self):
            
            sql = f'''
            SELECT * FROM "autores"
            ORDER BY "autor_id" ASC
            '''
            return sql