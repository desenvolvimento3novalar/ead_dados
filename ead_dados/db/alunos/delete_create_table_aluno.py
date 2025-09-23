import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from log.log import log
import psycopg2
from sqlalchemy.orm import sessionmaker


load_dotenv()

    
db = os.getenv("DB")

# Criar uma tabela
def criar_tabela_aluno():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()

        # SQL para criar a tabela
        criar_tabela_sql = """
        CREATE TABLE ead_dados.alunos (
	aluno_id int4 NOT NULL,
	nome varchar(255) NULL,
	email varchar(255) NULL,
	username varchar(100) NULL,
	tipo int4 NULL,
	data_cadastro timestamp NULL,
	status int4 NULL,
	cpf varchar(50) NULL,
	profissao varchar(100) NULL,
	biografia text NULL,
	curriculum text NULL,
	personalizado text NULL,
	anotacoes text NULL,
	nascimento date NULL,
	cidade varchar(100) NULL,
	uf bpchar(50) NULL,
	telefone varchar(50) NULL,
	cep varchar(50) NULL,
	endereco varchar(255) NULL,
	numero varchar(50) NULL,
	complemento varchar(100) NULL,
	bairro varchar(100) NULL,
	site varchar(255) NULL,
	twitter varchar(255) NULL,
	facebook varchar(255) NULL,
	linkedin varchar(255) NULL,
	youtube varchar(255) NULL,
	instagram varchar(255) NULL,
	tiktok varchar(255) NULL,
	ultimo_acesso timestamp NULL,
	foto varchar(500) NULL,
    campos_personalizados text NULL,
	campos_personalizados_decoded text NULL,
	CONSTRAINT aluno_pkey PRIMARY KEY (aluno_id)
);
        """
        session.execute(text(criar_tabela_sql))
        session.commit()
        log.info("Tabela criada com sucesso!")
    except Exception as e:
        log.error(f"Erro ao criar a tabela: {e}")
    finally:
        session.close()


# Excluir (DROP) uma tabela
def excluir_tabela_aluno():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()
        
        # SQL para excluir a tabela
        excluir_tabela_sql = "DROP TABLE ead_dados.alunos;"
        session.execute(text(excluir_tabela_sql))
        session.commit()
        log.info("Tabela excluída com sucesso!")
    except Exception as e:
        log.error(f"Erro ao excluir a tabela: {e}")
    finally:
        session.close()


