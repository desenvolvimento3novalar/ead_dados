import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from log.log import log
import psycopg2
from sqlalchemy.orm import sessionmaker


load_dotenv()

    
db = os.getenv("DB")

# Criar uma tabela
def criar_tabela_grupos():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()

        # SQL para criar a tabela
        criar_tabela_sql = """
        CREATE TABLE ead_dados.grupos (
	grupo_id int4 NOT NULL,
	grupo_nome varchar NOT NULL,
    status int4 NOT NULL,
	CONSTRAINT grupos_pk PRIMARY KEY (grupo_id)
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
def excluir_tabela_grupos():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()
        
        # SQL para excluir a tabela
        excluir_tabela_sql = "DROP TABLE IF EXISTS ead_dados.grupos;"
        session.execute(text(excluir_tabela_sql))
        session.commit()
        log.info("Tabela excluída com sucesso!")
    except Exception as e:
        log.error(f"Erro ao excluir a tabela: {e}")
    finally:
        session.close()


