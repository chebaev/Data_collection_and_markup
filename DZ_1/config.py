import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import SecretStr, StrictStr

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Configs(BaseSettings):
    api_key: SecretStr = os.getenv("API_KEY", None)
    url: StrictStr = os.getenv("URL", None)
    
    


