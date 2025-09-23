import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from log.log import log
import psycopg2
from sqlalchemy.orm import sessionmaker


load_dotenv()

    
db = os.getenv("DB")

# Criar uma tabela
def criar_tabela_progresso_aluno():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()

        # SQL para criar a tabela
        criar_tabela_sql = """
        CREATE TABLE ead_dados.progresso_aluno (
	progresso_id serial4 NOT NULL,
    matricula_id int4 NULL,
	curso_id int4 NULL,
	curso_titulo varchar(255) NULL,
	aluno_id serial4 NOT NULL,
	aluno_nome varchar(255) NULL,
	total_aulas int4 NULL,
	aulas_acessadas int4 NULL,
	progresso int4 NULL,
	visualizacoes int4 NULL,
	suporte int4 NULL,
	ultimo_acesso timestamp NULL,
	carga_horaria varchar(255) NULL,
	CONSTRAINT progresso_aluno_pkey PRIMARY KEY (progresso_id)
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
def excluir_tabela_progresso_aluno():
    try:
        # Conectar ao banco de dados
        engine = create_engine(db)

        Session = sessionmaker(bind=engine)
        session = Session()
        
        # SQL para excluir a tabela
        excluir_tabela_sql = "DROP TABLE IF EXISTS ead_dados.progresso_aluno;"
        session.execute(text(excluir_tabela_sql))
        session.commit()
        log.info("Tabela excluída com sucesso!")
    except Exception as e:
        log.error(f"Erro ao excluir a tabela: {e}")
    finally:
        session.close()


