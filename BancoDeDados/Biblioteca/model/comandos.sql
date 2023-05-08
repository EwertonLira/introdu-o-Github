/* Esses códigos estão organizados de acordo da seguinte maneira:

{livroIDSelect} códigos SQL create table
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
    "cliente_cpf" char({livroIDSelect}{livroIDSelect}) NOT NULL,
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
-- splitKeyComment select ID

SELECT * FROM "autores"
    WHERE "autor_id" = '{autorIdSelect}'

-- splitKeyComment select ID

SELECT * FROM "livros"
    WHERE "livro_id" = '{livroIDSelect}'

-- splitKeyComment select ID

SELECT * FROM "clientes"
    WHERE "cliente_id" = '{clienteIdSelect}'

-- splitKeyComment select ID

SELECT * FROM "aluguel"
    WHERE "aluguel_id" = '{aluguelIdSelect}'

-- splitKeyComment select ID
-- splitKeyComment insert

INSERT INTO "autores"
    Values(default, '{autorNomeInsert}')

-- splitKeyComment insert

INSERT INTO "livros"
    Values(default, '{livroNomeInsert}', '{livroPaginasInsert}','{livroAnoLancamentoInsert}','{livroAutorInsertFK}' )

-- splitKeyComment insert

INSERT INTO "clientes"
    Values(default, '{clienteNomeInsert}', '{clienteCpfInsert}', '{clienteTelefoneInsert}','{clienteEmailInsert}', '{clienteNascimentoInsert}' )

-- splitKeyComment insert

INSERT INTO "aluguel"
    Values(default, '{clienteIdInsertFK}', '{livroIdInsertFK}', '{aluguelDataRetiradaInsert}','{aluguelDataEntregaInsert}', '{aluguelNotificacaoInsert}' )

-- splitKeyComment insert
-- splitKeyComment update

UPDATE "autores"
    SET "autor_nome" = '{autorNomeUpdate}'       
    WHERE "autor_id" = '{autorIdEscolhidoUpdate}';

-- splitKeyComment update

UPDATE "livros"
    SET "livro_nome" = '{livroNomeUpdate}'
        "livro_Paginas" = '{livroPaginasUpdate}'
        "livro_ano_lancamento" = '{livroAnoLancamentoUpdate}'
        "livro_autor" = '{livroAutorUpdateFK}'    
    WHERE "livro_id" = '{livroIdEscolhidoUpdate}';

-- splitKeyComment update

UPDATE "clientes"
    SET "cliente_nome" = '{clienteNomeUpdate}'
        "cliente_cpf" = '{clienteCpfUpdate}'
        "cliente_telefone" = '{clienteTelefoneUpdate}'
        "cliente_email" = '{clienteEmailUpdate}'
        "cliente_nascimento" = '{clienteNascimentoUpdate}'    
    WHERE "cliente_id" = '{clienteIdEscolhidoUpdate}';

-- splitKeyComment update

UPDATE "aluguel"
    SET "clienteIdFK" = '{clienteIdUpdateFK}'
        "livroIdFK" = '{livroIdUpdateFK}'
        "aluguelDataRetirada" = '{aluguelDataRetiradaUpdate}'
        "aluguelDataEntrega" = '{aluguelDataEntregaUpdate}'
        "aluguelNotificacao" = '{aluguelNotificacaoUpdate}'    
    WHERE "aluguel_id" = '{aluguelIdEscolhidoUpdate}';

-- splitKeyComment update
-- splitKeyComment delete

 DELETE 
    FROM "autores"
    WHERE "autor_id" = '{autorIdEscolhidoDelete}';

-- splitKeyComment delete

 DELETE 
    FROM "livros"
    WHERE "livro_id" = '{livroIdEscolhidoDelete}';

-- splitKeyComment delete

 DELETE 
    FROM "clientes"
    WHERE "cliente_id" = '{clienteIdEscolhidoDelete}';

-- splitKeyComment delete

 DELETE 
    FROM "aluguel"
    WHERE "aluguel_id" = '{aluguelIdEscolhidoDelete}';

-- splitKeyComment delete