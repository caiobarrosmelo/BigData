import sys
import requests
from pathlib import Path

# Adiciona o diretório raiz do projeto ao path
# Sobe até a pasta BigData (raiz do projeto)
root_path = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_path))

from AtividadePratica4.app.models.cambio import Cambio

# Service to handle API data collection and preprocessing
class CambioService:
    
    def __init__(self, api_url, preprocessor): 
        self.api_url = api_url                   
        self.preprocessor = preprocessor        
        
    def fetch_and_preprocess(self):
        response = requests.get(self.api_url)   
        response.raise_for_status()
        data = response.json()
        raw_data = data.get("value", [])     
        
        # Preprocess each item from the response
        processed = [self.preprocessor.process(item) for item in raw_data]  
        return processed