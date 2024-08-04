import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    config = {
        'TOKEN': os.getenv('TOKEN')
    }
    if not config['TOKEN']:
        raise ValueError("No se encontró el token en el archivo .env")
    return config