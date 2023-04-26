from control.classConexao import *

lojaBanco = conexao("loja","localhost","5432","postgres","postgre") # conexão criada

lojaBanco.manipularBanco('''
    
    CREATE TABLE "Cliente" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" VARCHAR(255) NOT NULL,
    );

''')

lojaBanco.manipularBanco(''' 
    
    CREATE TABLE "Produto" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome produto" VARCHAR(255) NOT NULL,
    "Preço Produto" INT NOT NULL,
    "Estoque Produto" INT NOT NULL DEFAULT 0,

    );
''')

lojaBanco.manipularBanco(''' 
    
    CREATE TABLE "Compra" (
    "Id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Id_Cliente" INT NOT NULL,
    "Id_Produto" INT NOT NULL,
    "Quantidade" INT NOT NULL,
    "Valor Total" INT NOT NULL,
    "TimesTamp" TIMESTAMP DEFAULT CURRENT_TIMESTAMP(0),
        
        CONSTRAINT fk_Cliente
            FOREIGN KEY("Id_Cliente")
            REFERENCES "Cliente"("Id")
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
    
    );
''')
