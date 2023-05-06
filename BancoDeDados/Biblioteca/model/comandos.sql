/* Esses códigos estão organizados de acordo da seguinte maneira:

1 códigos SQL create table
2 códigos SQL select
3 códigos SQL insert
4 códigos SQL update
5 códigos SQL delete

todas as tabelas criadas tem seus respectivos códgiso SQL
separados por splitkeycomment  que servem para separar os trechos de códigos
em elementos de uma listas quando for usado o comando split() em python

os trechos de códigos SQL serão chamados pelo comando open() em python e modificados
de acordo com a sua utilização

depois de salvo as alterações no techo de código SQL, pode ser chamado
para dentro do script em pytho e ser feitas utilizações.

todas as variáveis que iniciam com aspas simples e chave e terminam com chaves e aspas siples
são variáveis para prencher com valores através dos script de python
>>> '{name}'
>>> '{example}'

*/

-- splitKeyComment table

CREATE TABLE "autores" (
    "autor_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "autor_nome" varchar(255) NOT NULL
);

-- splitKeyComment table

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

-- splitKeyComment table

CREATE TABLE "clientes" (
    "cliente_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_nome" varchar(255) NOT NULL,
    "cliente_cpf" char(11) NOT NULL,
    "cliente_telefone" varchar(255), NOT NULL DEFAULT 'não informado',
    "cliente_email" varchar(255) NOT NULL DEFAULT 'não informado',
    "cliente_nascimento" date
);

-- splitKeyComment table

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

-- splitKeyComment table
-- splitKeyComment select

SELECT * FROM "autores"
    ORDER BY "autor_id" ASC

-- splitKeyComment select

SELECT * FROM "livros"
    ORDER BY "livro_id" ASC

-- splitKeyComment select

SELECT * FROM "clientes"
    ORDER BY "cliente_id" ASC

-- splitKeyComment select

SELECT * FROM "aluguel"
    ORDER BY "aluguel_id" ASC

-- splitKeyComment select
-- splitKeyComment insert

INSERT INTO "autores"
    Values(default, '{autor_nome}')

-- splitKeyComment insert

INSERT INTO "livros"
    Values(default, '{livroNome}', '{livroPaginas}','{livroAnoLancamento}','{livroAutorFK}' )

-- splitKeyComment insert

INSERT INTO "clientes"
    Values(default, '{clienteNome}', '{clienteCpf}', '{clienteTelefone}','{clienteEmail}', '{clienteNascimento}' )

-- splitKeyComment insert

INSERT INTO "aluguel"
    Values(default, '{clienteIdFK}', '{livroIdFK}', '{aluguelDataRetirada}','{aluguelDataEntrega}', '{aluguelNotificacao}' )

-- splitKeyComment insert
-- splitKeyComment update

UPDATE "autores"
    SET "autor_nome" = 'Paulo de tarso'       
    WHERE "autor_id" = '{autorIdEscolhido}';

-- splitKeyComment update

UPDATE "livros"
    SET "livro_nome" = '{livroNome}'
        "livro_Paginas" = '{livroPaginas}'
        "livro_ano_lancamento" = '{livroAnoLancamento}'
        "livro_autor" = '{livroAutorFK}'    
    WHERE "livro_id" = '{livroIdEscolhido}';

-- splitKeyComment update

UPDATE "clientes"
    SET "cliente_nome" = '{clienteNome}'
        "cliente_cpf" = '{clienteCpf}'
        "cliente_telefone" = '{clienteTelefone}'
        "cliente_email" = '{clienteEmail}'
        "cliente_nascimento" = '{clienteNascimento}'    
    WHERE "cliente_id" = '{clienteIdEscolhido}';

-- splitKeyComment update

UPDATE "aluguel"
    SET "clienteIdFK" = '{clienteIdFK}'
        "livroIdFK" = '{livroIdFK}'
        "aluguelDataRetirada" = '{aluguelDataRetirada}'
        "aluguelDataEntrega" = '{aluguelDataEntrega}'
        "aluguelNotificacao" = '{aluguelNotificacao}'    
    WHERE "aluguel_id" = '{aluguelIdEscolhido}';

-- splitKeyComment update
-- splitKeyComment delete

 DELETE 
    FROM "autores"
    WHERE "autor_id" = '{autorIdEscolhido}';

-- splitKeyComment delete

 DELETE 
    FROM "livros"
    WHERE "livro_id" = '{livroIdEscolhido}';

-- splitKeyComment delete

 DELETE 
    FROM "clientes"
    WHERE "cliente_id" = '{clienteIdEscolhido}';

-- splitKeyComment delete

 DELETE 
    FROM "aluguel"
    WHERE "aluguel_id" = '{aluguelIdEscolhido}';

-- splitKeyComment delete