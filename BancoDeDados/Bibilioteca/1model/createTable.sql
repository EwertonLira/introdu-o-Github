CREATE TABLE "autores" (
    "autor_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "autor_nome" varchar(255) NOT NULL
);

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

CREATE TABLE "clientes" (
    "cliente_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_nome" varchar(255) NOT NULL,
    "cliente_cpf" char(11) NOT NULL,
    "cliente_telefone" varchar(255), NOT NULL DEFAULT 'não informado',
    "cliente_email" varchar(255) NOT NULL DEFAULT 'não informado',
    "cliente_nascimento" date
);

CREATE TABLE "aluguel" (
    "aluguel_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int,
    "livro_id" int,
    "aluguel_data_retirada" date,
    "aluguel_data_entrega" date,
    "aluguel_notificacao" varchar(255),
    
    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id"),
    
    CONSTRAINT fk_livro
        FOREIGN KEY ("livro_id")
        REFERENCES "livros"("livro_id")
);