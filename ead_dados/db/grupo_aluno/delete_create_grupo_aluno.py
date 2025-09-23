import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from log.log import log
import psycopg2
from sqlalchemy.orm import sessionmaker


load_dotenv()

    
db = os.getenv("DB")

# Criar uma tabela
def criar_tabela_grupo_aluno():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()

        # SQL para criar a tabela
        criar_tabela_sql = """
        CREATE TABLE ead_dados.grupo_aluno (
grupo_aluno_id serial8 not null,
	grupo_id int8 NOT NULL,
	grupo_nome varchar(255) NULL,
	aluno_id int4 NULL,
	name varchar(255) NULL,
	email varchar(255) null,
	CONSTRAINT grupo_aluno_pkey PRIMARY KEY (grupo_aluno_id)
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
def excluir_tabela_grupo_aluno():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()
        
        # SQL para excluir a tabela
        excluir_tabela_sql = "DROP TABLE ead_dados.grupo_aluno;"
        session.execute(text(excluir_tabela_sql))
        session.commit()
        log.info("Tabela excluída com sucesso!")
    except Exception as e:
        log.error(f"Erro ao excluir a tabela: {e}")
    finally:
        session.close()


