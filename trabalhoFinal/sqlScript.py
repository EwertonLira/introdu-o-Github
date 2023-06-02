# tudo em uma strig.
sqltabelas = '''
-- BEGIN;
CREATE TABLE "endereco" (
    "endereco_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "endereco_cep" varchar(255) NOT NULL,
    "endereco_uf" varchar(255),
    "endereco_cidade" varchar(255),
    "endereco_bairro" varchar(255),
    "endereco_nome" varchar(255),
    "endereco_complemento" varchar(255),
    "endereco_status" varchar(255) NOT NULL DEFAULT 'ativo'
);

CREATE TABLE "cliente" (
    "cliente_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_nome" varchar(255) NOT NULL,
    "cliente_telefone" varchar(15) NOT NULL,
    "cliente_email" varchar(255) UNIQUE,
    "cliente_endereco" int,
    "cliente_status" varchar(255) NOT NULL DEFAULT 'ativo',
        CONSTRAINT fk_endereco
            FOREIGN KEY ("cliente_endereco")
            REFERENCES "endereco"("endereco_id")
);

CREATE TABLE "orcamento" (
    "orcamento_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int,
    "orcamento_media_energia" decimal (10,2),
    "orcamento_media_pagamento_energia" decimal (10,2),
    "orcamento_tipo_residencia" varchar(255),
    "orcamento_valor_instalacao" decimal (10,2),
    "orcamento_data" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "orcamento_status" varchar(255) NOT NULL DEFAULT 'ativo',
        CONSTRAINT fk_cliente
            FOREIGN KEY ("cliente_id")
            REFERENCES "cliente"("cliente_id")
);

CREATE TABLE "cartao" (
    "cartao_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cartao_numero" varchar(255),
    "cartao_bandeira" varchar(255),
    "cartao_ccv" varchar (255),
    "cartao_validade" varchar (255),
    "cartao_descricao" varchar(255),
    "cartao_status" varchar(255) NOT NULL DEFAULT 'ativo' 
);

CREATE TABLE "banco" (
    "banco_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "banco_nome" varchar(255),
    "banco_banco" varchar (255),
    "banco_descricao" varchar(255),
    "banco_status" varchar(255) NOT NULL DEFAULT 'ativo'
);

CREATE TABLE "pagamento" (
    "pagamento_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cartao_id" int,
    "pagamento_forma" varchar(255),
    "pagamento_valor" decimal (10,2),
    "pagamento_Bandeira_cartao" varchar(255),
    "banco_id" int,
    "pagamento_descricao" varchar(255),
    "pagamento_status" varchar(255) NOT NULL DEFAULT 'ativo',
        CONSTRAINT fk_cartao
            FOREIGN KEY ("cartao_id")
            REFERENCES "cartao"("cartao_id"),
        CONSTRAINT fk_banco
            FOREIGN KEY ("banco_id")
            REFERENCES "banco"("banco_id")
);

CREATE TABLE "pedido" (
    "pedido_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int,
    "orcamento_id" int,
    "pagamento_id" int,
    "pedido_data" timestamp NOT NULL DEFAULT (CURRENT_TIMESTAMP),
    "pedido_status" varchar(255) NOT NULL DEFAULT 'ativo',
        CONSTRAINT fk_cliente
            FOREIGN KEY ("cliente_id")
            REFERENCES "cliente"("cliente_id"),
        CONSTRAINT fk_orcamento
            FOREIGN KEY ("orcamento_id")
            REFERENCES "orcamento"("orcamento_id"),
        CONSTRAINT fk_pagamento
            FOREIGN KEY ("pagamento_id")
            REFERENCES "pagamento"("pagamento_id")
);

CREATE TABLE "produto" (
    "produto_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "produto_nome" varchar(255),
    "produto_valor" decimal (10,2),
    "produto_descricao" varchar(255),
    "produto_imagem" bytea CHECK (octet_length("produto_imagem") <= 52428800), -- Limite de 50 MB
    "produto_status" varchar(255) NOT NULL DEFAULT 'ativo'
);

-- COMMIT;
'''