from control.classConexao import *

lojaBanco = Conexao("loja","localhost","5432","postgres","postgre") # conexão criada

# tabela cliente
lojaBanco.manipularBanco('''
    
    CREATE TABLE "Cliente" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" VARCHAR(255) NOT NULL,
    );

''')

# tabela Produto
lojaBanco.manipularBanco(''' 
    
    CREATE TABLE "Produto" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome produto" VARCHAR(255) NOT NULL,
    "Preço Produto" NUMERIC(2) NOT NULL,
    "Estoque Produto" INT NOT NULL DEFAULT 0,

    );
''')

# tabela Compra
lojaBanco.manipularBanco(''' 
    
    CREATE TABLE "Compra" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Id_Cliente" INT NOT NULL,
    "Id_Produto" INT NOT NULL,
    "Quantidade" INT NOT NULL,
    "Valor Total" NUMERIC(2) NOT NULL,
    "TimesTamp" TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0),
        
        CONSTRAINT fk_Cliente
            FOREIGN KEY("Id_Cliente")
            REFERENCES "Produto"("Id")
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
            ,

        CONSTRAINT fk_produto
            FOREIGN KEY("Id_Produto")
            REFERENCES "Cliente"("Id")

    
    );
''')

# inserir Lista de Clientes
lojaBanco.manipularBanco('''
    INSERT INTO "Cliente"
    VALUES (DEFAULT,"José da silva),
        (DEFAULT,"silva),
        (DEFAULT,"José),
        (DEFAULT,"Pedro"),
        (DEFAULT,"Paulo"),
        (DEFAULT,"Ana Paula"),
        (DEFAULT,"Maria);
''')

def inserirCliente():
    
    lojaBanco.manipularBanco('''
    INSERT INTO "Cliente"
    VALUES (DEFAULT,"José da silva),
        (DEFAULT,"silva),
        (DEFAULT,"José),
        (DEFAULT,"Pedro"),
        (DEFAULT,"Paulo"),
        (DEFAULT,"Ana Paula"),
        (DEFAULT,"Maria);
''')