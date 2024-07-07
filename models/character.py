import requests
import os
import random
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class Character:
    url = os.getenv("BASE_URL")
    type = os.getenv("TOKEN_TYPE")
    token = os.getenv("TOKEN")

    @staticmethod
    def get_random_character():
        headers = {
            'Authorization': f'{Character.type} {Character.token}'
        }
        response = requests.get(f"{Character.url}/character",headers=headers)
        logger.info('A requisicao para buscar um personagem retornou {response.status_code}!')
        if response.status_code == 200:
            data = response.json()
            character = data.get("docs",[])
            index = random.randint(0,934)
            logger.info(f'O index foi: {index}')
            if character:
                return character[index]["name"]
            return "Sorry my dear fellow, no character was found, try again later."
        
    @staticmethod
    def get_specifc_character(name):
        fm_name = name.capitalize()
        headers = {
            'Content-type':'application/json',
            'Authorization':f'{Character.type} {Character.token}'
        }
        query = {'name':fm_name}
        response = requests.get(f"{Character.url}/character?",headers=headers,params=query)
        res = response.status_code
        logger.info(f'A requisicao para buscar um personagem retornou {res}!')
        if response.status_code == 200:
            data = response.json()
            spf_character = data.get("docs",[])
            if spf_character:
                return spf_character
            else:
                return {'Erro': 'Personagem não econtrado'}
        else:
            return {'Erro': f'{res}'}

