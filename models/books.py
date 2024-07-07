import requests
import os
import random
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class Books:
    url = os.getenv('BASE_URL')
    type = os.getenv('TOKEN_TYPE')
    token = os.getenv('TOKEN')

    def get_books():
        headers = {
            'Content-Type':'application/json',
            'Authorization': f'{Books.type} {Books.token}'
        }
        response = requests.request("GET",url=f'{Books.url}/book',headers=headers)
        res = response.status_code
        if res == 200:
            data = response.json()
            book = data.get("docs",[])
            if book:
                return book
            else:
                return {'Erro': 'Não foi possível encontrar livros.'}
        else:
            return {'Erro': f'{res}'}