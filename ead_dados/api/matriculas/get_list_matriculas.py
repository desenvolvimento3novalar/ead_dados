from log.log import log
import os
from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException

def get_list_matriculas():
    # Carregar as variáveis do .env
    load_dotenv()

    api_key = os.getenv("API_KEY")
    offset = 0
    limit = 900
    max_retries = 3  # Número máximo de tentativas por offset

    list_cpf = []

    while True:
        
        url = f'https://novalar.eadplataforma.app/api/1/enrollment?limit={limit}&offset={offset}'

        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(url, headers={
                    'x-auth-token': api_key,
                    'accept': 'application/json'
                }, timeout=60)  # Timeout de 10 segundos


                if response.status_code == 204:
                    log.info("Nenhum conteúdo retornado. Encerrando busca.")
                    return list_cpf

                response.raise_for_status()  

                try:
                    data = response.json()
                except Exception as e:
                    log.error(f"Erro ao decodificar JSON: {e}")
                    return list_cpf
    
                if not isinstance(data, list) or not data:
                    log.info(f"Nenhum dado válido no offset {offset}. Encerrando busca.")
                    return list_cpf

                for student in data:
                    list_cpf.append(student)
                    
                offset += limit  # Próximo lote

                retries = 3 
            except RequestException as e:
                retries += 1
                log.warning(f"Erro de conexão (tentativa {retries}/{max_retries}) no offset {offset}: {e}")

        

