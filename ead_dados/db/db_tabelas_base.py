from datetime import datetime
import os
import re
from dotenv import load_dotenv
from log.log import log
from sqlalchemy import Column, Integer, String, Numeric, Date, Interval, Text, DateTime, create_engine, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# ===========================
# TABELA ALUNO
# ===========================
class Aluno(Base):
    __tablename__ = 'alunos'
    __table_args__ = {'schema': 'ead_dados'}  
    
    aluno_id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    email = Column(String(255))
    username = Column(String(100))
    tipo = Column(Integer)
    data_cadastro = Column(DateTime)
    status = Column(Integer)
    cpf = Column(String(50))
    profissao = Column(String(100))
    biografia = Column(Text)
    curriculum = Column(Text)
    personalizado = Column(Text)
    anotacoes = Column(Text)
    nascimento = Column(Date)
    cidade = Column(String(100))
    uf = Column(String(50))
    telefone = Column(String(50))
    cep = Column(String(50))
    endereco = Column(String(255))
    numero = Column(String(50))
    complemento = Column(String(100))
    bairro = Column(String(100))
    site = Column(String(255))
    twitter = Column(String(255))
    facebook = Column(String(255))
    linkedin = Column(String(255))
    youtube = Column(String(255))
    instagram = Column(String(255))
    tiktok = Column(String(255))
    ultimo_acesso = Column(DateTime)
    foto = Column(String(500))
    campos_personalizados = Column(Text)
    campos_personalizados_decoded = Column(JSON)


def add_data_aluno(lista):
    load_dotenv()
    db = os.getenv("DB")
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for user in lista:
        novo = Aluno(**user)
        session.add(novo)
        session.commit()
        log.info(f"{user['nome']} adicionado com sucesso!")

    session.close()


# ===========================
# TABELA MATRICULAS
# ===========================
class Matriculas(Base):
    __tablename__ = 'matriculas'
    __table_args__ = {'schema': 'ead_dados'}  

    matricula_id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer)
    aluno_nome = Column(String(255))
    aluno_email = Column(String(255))
    curso_id = Column(Integer)
    titulo_curso = Column(String(255))
    emitir_certificado = Column(Integer)
    cadastro = Column(DateTime)
    inicio = Column(DateTime)
    suporte = Column(DateTime)
    expira = Column(DateTime)
    status = Column(Integer)
    assinatura_id = Column(Integer)
    cupom = Column(String(100))
    origem = Column(Integer)
    grupo_id = Column(Integer)
    grupo_nome = Column(String(255))


def add_data_matriculas(lista):
    load_dotenv()
    db = os.getenv("DB")
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for user in lista:
        novo = Matriculas(**user)
        session.add(novo)
        session.commit()
        log.info(f"Matricula {user['matricula_id']} adicionada com sucesso!")

    session.close()


# ===========================
# TABELA PROGRESSO_ALUNO
# ===========================
class ProgressoAluno(Base):
    __tablename__ = 'progresso_aluno'
    __table_args__ = {'schema': 'ead_dados'}  

    progresso_id = Column(Integer, primary_key=True)
    matricula_id = Column(Integer)
    curso_id = Column(Integer)
    curso_titulo = Column(String(255))
    aluno_id = Column(Integer)
    aluno_nome = Column(String(255))
    total_aulas = Column(Integer)
    aulas_acessadas = Column(Integer)
    progresso = Column(Integer)
    visualizacoes = Column(Integer)
    suporte = Column(Integer)
    ultimo_acesso = Column(DateTime)
    carga_horaria = Column(String(255))
    situacao = Column(String(255))



def add_data_progresso_aluno(lista):
    load_dotenv()
    db = os.getenv("DB")
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for user in lista:
        novo = ProgressoAluno(**user)
        session.add(novo)
        session.commit()
        log.info(f"Progresso {user['aluno_nome']} adicionado com sucesso!")

    session.close()


# ===========================
# TABELA CERTIFICADO
# ===========================
class Certificado(Base):
    __tablename__ = 'certificados'
    __table_args__ = {'schema': 'ead_dados'}  

    id = Column(Integer, primary_key=True)
    hash = Column(String(255))
    curso_id = Column(Integer)
    curso_titulo = Column(String(255))
    aluno_id = Column(Integer)
    aluno_nome = Column(String(255))
    media_final = Column(Numeric(5, 2))
    iniciado = Column(DateTime)
    concluido = Column(DateTime)
    carga_horaria = Column(String(50))
    certificado_link = Column(String(500))
    certificado_pdf = Column(String(500))


def add_data_certificado(lista):
    load_dotenv()
    db = os.getenv("DB")
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for user in lista:
        novo = Certificado(**user)
        session.add(novo)
        session.commit()
        log.info(f"Certificado {user['id']} adicionado com sucesso!")

    session.close()


# ===========================
# TABELA GRUPO
# ===========================
class Grupo(Base):
    __tablename__ = 'grupos'
    __table_args__ = {'schema': 'ead_dados'}  

    grupo_id = Column(Integer, primary_key=True)
    grupo_nome = Column(String(255))
    status = Column(Integer)


def add_data_grupo(lista):
    load_dotenv()
    db = os.getenv("DB")
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for user in lista:
        novo = Grupo(**user)
        session.add(novo)
        session.commit()
        log.info(f"Grupo {user['grupo_nome']} adicionado com sucesso!")

    session.close()


# ===========================
# TABELA GRUPO_ALUNO
# ===========================
class GrupoAluno(Base):
    __tablename__ = 'grupo_aluno'
    __table_args__ = {'schema': 'ead_dados'}  
    grupo_aluno_id = Column(Integer, primary_key=True)
    grupo_id = Column(Integer)
    grupo_nome = Column(String(255))
    aluno_id = Column(Integer)
    name = Column(String(255))
    email = Column(String(255))


def add_data_grupo_aluno(lista):
    load_dotenv()
    db = os.getenv("DB")
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for user in lista:
        novo = GrupoAluno(**user)
        session.add(novo)
        session.commit()
        log.info(f"Aluno {user['name']} adicionado ao grupo {user['grupo_nome']}!")

    session.close()
