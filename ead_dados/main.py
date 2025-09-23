
from ead_dados.api.certificados.get_list_certificados import get_list_certificados
from ead_dados.api.grupo_aluno.get_list_grupo_aluno import get_list_grupo_aluno
from ead_dados.api.grupos.get_list_grupos import get_list_grupos
from db.db_tabelas_base import add_data_certificado, add_data_grupo, add_data_aluno, add_data_grupo_aluno, add_data_matriculas, add_data_progresso_aluno
from db.grupos.delete_create_table_grupos import criar_tabela_grupos, excluir_tabela_grupos
from db.alunos.delete_create_table_aluno import criar_tabela_aluno, excluir_tabela_aluno
from ead_dados.api.alunos.get_list_alunos import get_list_alunos
from ead_dados.api.matriculas.get_list_matriculas import get_list_matriculas
from ead_dados.api.progresso_aluno.get_list_progresso_aluno import get_list_progresso_aluno
from ead_dados.db.certificados.delete_create_table_certificados import criar_tabela_certificados, excluir_tabela_certificados
from ead_dados.db.grupo_aluno.delete_create_grupo_aluno import criar_tabela_grupo_aluno, excluir_tabela_grupo_aluno
from ead_dados.db.matriculas.delete_create_table_matriculas import criar_tabela_matriculas, excluir_tabela_matriculas
from ead_dados.db.progresso_aluno.delete_create_progresso_aluno import criar_tabela_progresso_aluno, excluir_tabela_progresso_aluno


list_groups = get_list_grupos()


if (isinstance(list_groups, list) ):
    list_grupo_aluno = get_list_grupo_aluno(list_groups)
    list_aluno = get_list_alunos() 
    list_matriculas = get_list_matriculas()
    list_certificados = get_list_certificados()
    list_progresso = get_list_progresso_aluno()
    if (isinstance(list_grupo_aluno, list) and isinstance(list_aluno, list) 
        and isinstance(list_groups, list) and isinstance(list_matriculas, list) 
        and isinstance(list_certificados, list) and isinstance(list_progresso, list)):
    
        excluir_tabela_grupos()
        criar_tabela_grupos()
        add_data_grupo(list_groups)


        excluir_tabela_grupo_aluno()
        criar_tabela_grupo_aluno()
        add_data_grupo_aluno(list_grupo_aluno)


        excluir_tabela_aluno()
        criar_tabela_aluno()
        add_data_aluno(list_aluno)

        excluir_tabela_matriculas()
        criar_tabela_matriculas()
        add_data_matriculas(list_matriculas)

        excluir_tabela_certificados()
        criar_tabela_certificados()
        add_data_certificado(list_certificados)

        excluir_tabela_progresso_aluno()
        criar_tabela_progresso_aluno()
        add_data_progresso_aluno(list_progresso)
    
        

            