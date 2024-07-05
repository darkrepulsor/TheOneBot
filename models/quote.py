import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Quote:
    url = os.getenv("BASE_URL")
    type = os.getenv("TOKEN_TYPE")
    token = os.getenv("TOKEN")

    @staticmethod
    def get_random_quote():
        headers = {
            'Authorization: f{Quote.type} {Quote.token}'
        }
        response = requests.get(f"{Quote.url}/quote",headers=headers)
        if response.status_code == 200:
            data = response.json()
            quotes = data.get("docs",[])
            if quotes:
                return quotes[0]["dialog"]
        return "No quote found"