# arquivo python que gera arquivos de texto SQL para criar tabelas
# essas funções devem ser usado com a conexão banco.
import json

def CriarTodasTabelas(biblioBD):
    # função só funciona uma vez depois buga.
    # esta função serve para criar todas as tabelas que existe nesse arquivo. precisa importar classConexão e json
    try:
        with open("control\statusTabelas.json", 'r') as arquivoJson:
            chave = json.load(arquivoJson)
    
        if chave["status"] == "criada":
            pass
    except:
        try:
            biblioBD.manipularBanco(criarTabelaAutor())
            biblioBD.manipularBanco(criarTabelaLivro())
            biblioBD.manipularBanco(criarTabelaCliente())
            biblioBD.manipularBanco(criarTabelaAluguel())

            statusTabela = { "status" : "criada" }
            with open("control\statusTabelas.json", 'w') as arquivoJson:
                json.dump(statusTabela , arquivoJson, indent=2)
        except:
            print("verfique o banco de dados")

#__________________ tabelas sql __________________________

def criarTabelaAutor():
    sql ='''CREATE TABLE "autores" (
    "autor_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "autor_nome" varchar(255) NOT NULL
    );
    '''
    return sql

def criarTabelaLivro():
    sql = '''CREATE TABLE "livros" (
    "livro_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "livro_nome" varchar(255) NOT NULL,
    "livro_paginas" varchar(255) NOT NULL DEFAULT 'não informado',
    "livro_ano_lancamento" varchar(255) NOT NULL DEFAULT 'não informado',
    "livro_autor" int NOT NULL,
    "livro_status" varchar(255),
    CONSTRAINT fk_autor
        FOREIGN KEY ("livro_autor")
        REFERENCES "autores"("autor_id")
    );
    '''
    return sql


def criarTabelaCliente():
    sql = '''CREATE TABLE "clientes" (
    "cliente_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_nome" varchar(255) NOT NULL,
    "cliente_cpf" char(11) NOT NULL,
    "cliente_telefone" varchar(255) NOT NULL DEFAULT 'não informado',
    "cliente_email" varchar(255) NOT NULL DEFAULT 'não informado',
    "cliente_nascimento" varchar(255),
    "cliente_status" varchar(255)
    );
    '''
    return sql


def criarTabelaAluguel():
    sql = '''CREATE TABLE "aluguel" (
    "aluguel_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int,
    "livro_id" int,
    "aluguel_data_retirada" varchar(255),
    "aluguel_data_entrega" varchar(255),
    "aluguel_notificacao" varchar(255),
    "aluguel_status" varchar(255),

    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id"),
    
    CONSTRAINT fk_livro
        FOREIGN KEY ("livro_id")
        REFERENCES "livros"("livro_id")
    );
    '''
    return sql
