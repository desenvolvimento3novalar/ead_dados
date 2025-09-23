import os

from dotenv import load_dotenv
import requests


def get_list_grupos():
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_ead_url = os.getenv("EAD_API_URL")




    r = requests.get(f'{api_ead_url}/group', headers={
            'x-auth-token': api_key, 'accept': 'application/json'},)


    if(r.status_code == 200):
        data = r.json()

        return data
