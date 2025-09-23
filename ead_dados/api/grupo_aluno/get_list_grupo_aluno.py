from log.log import log
import os
from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException
import time

def get_list_grupo_aluno(listgrupos):
    """
    Recebe uma lista de grupos no formato:
      [{'grupo_id': 1, 'grupo_nome': 'Alunos', 'status': 1}, ...]
    
    Retorna:
      Lista com todos os alunos de todos os grupos.
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        log.error("API_KEY não encontrada no .env")
        return []

    limit = 900
    max_retries = 3

    list_alunos = []
    seen_ids = set()   # para evitar duplicatas se aluno tiver campo 'id'

    for grupo in listgrupos:

        idgrupo = grupo.get("grupo_id")
        if not idgrupo:
            continue

        offset = 0
        while True:
            url = f'https://novalar.eadplataforma.app/api/1/groupstudent/{idgrupo}?limit={limit}&offset={offset}'
            finished = False

            for attempt in range(1, max_retries + 1):
                try:
                    response = requests.get(
                        url,
                        headers={'x-auth-token': api_key, 'accept': 'application/json'},
                        timeout=60
                    )

                    if response.status_code == 204:
                        log.info(f"Grupo {idgrupo} ({grupo.get('grupo_nome')}): Nenhum conteúdo retornado (204).")
                        finished = True
                        break

                    response.raise_for_status()

                    try:
                        data = response.json()
                    except Exception as e:
                        log.error(f"Grupo {idgrupo} offset {offset}: Erro ao decodificar JSON: {e}")
                        finished = True
                        break

                    if not isinstance(data, list) or not data:
                        log.info(f"Grupo {idgrupo} ({grupo.get('grupo_nome')}): sem dados válidos no offset {offset}.")
                        finished = True
                        break

                    # Processa alunos e evita duplicatas
                    for student in data:
                        sid = student.get("id")
                        if sid and sid in seen_ids:
                            continue
                        if sid:
                            seen_ids.add(sid)

                        list_alunos.append(student)

                    offset += limit
                    break  # sucesso, sai do loop de tentativas e busca próxima página

                except RequestException as e:
                    log.warning(
                        f"Grupo {idgrupo} — erro de conexão (tentativa {attempt}/{max_retries}) offset {offset}: {e}"
                    )
                    if attempt == max_retries:
                        log.error(f"Grupo {idgrupo} — falha após {max_retries} tentativas no offset {offset}. Pulando grupo.")
                        finished = True
                        break
                    time.sleep(1)  # pequena pausa antes da próxima tentativa

            if finished:
                break

    return list_alunos
