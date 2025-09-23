import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from log.log import log
import psycopg2
from sqlalchemy.orm import sessionmaker


load_dotenv()

    
db = os.getenv("DB")

# Criar uma tabela
def criar_tabela_certificados():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()

        # SQL para criar a tabela
        criar_tabela_sql = """
        CREATE TABLE ead_dados.certificados (
	id serial4 NOT NULL,
	hash varchar(255) NULL,
	curso_id int4 NULL,
	curso_titulo varchar(255) NULL,
	aluno_id int4 NULL,
	aluno_nome varchar(255) NULL,
	media_final numeric(5, 2) NULL,
	iniciado timestamp NULL,
	concluido timestamp NULL,
	carga_horaria varchar(50) NULL,
	certificado_link varchar(500) NULL,
	certificado_pdf varchar(500) NULL,
	CONSTRAINT certificado_pkey PRIMARY KEY (id)
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
def excluir_tabela_certificados():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()
        
        # SQL para excluir a tabela
        excluir_tabela_sql = "DROP TABLE ead_dados.certificados;"
        session.execute(text(excluir_tabela_sql))
        session.commit()
        log.info("Tabela excluída com sucesso!")
    except Exception as e:
        log.error(f"Erro ao excluir a tabela: {e}")
    finally:
        session.close()


