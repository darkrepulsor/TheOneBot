import requests
import os
import random
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class Quote:
    url = os.getenv("BASE_URL")
    type = os.getenv("TOKEN_TYPE")
    token = os.getenv("TOKEN")

    @staticmethod
    def get_random_quote():
        headers = {
            'Authorization': f'{Quote.type} {Quote.token}'
        }
        query = {'limit':'2500'}
        response = requests.get(f"{Quote.url}/quote",headers=headers,params=query)
        if response.status_code == 200:
            data = response.json()
            quotes = data.get("docs",[])
            index = random.randint(0,2384)
            logger.info(f'O index foi: {index}')
            if quotes:
                return quotes[index]["dialog"]
        return "No quote found"