import sys
from pathlib import Path

# Add project root directory to Python path
# Navigate up 3 levels: app/ → AtividadePratica4/ → BigData/
root_path = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_path))

from AtividadePratica4.app.config import Configuration
from AtividadePratica4.app.repositories.cambio_repository import CambioRepository
from AtividadePratica4.app.services.cambio_service import CambioService
from AtividadePratica4.app.preprocessors.cambio_preprocessor import CambioPreprocessor
from AtividadePratica4.app.utils.cambio_security import is_valid_uri

def main():
    # Validate database URI
    if not is_valid_uri(Configuration.MONGO_URI):
        raise ValueError("Invalid MONGO_URI!")

    # Initialize components
    repository = CambioRepository(Configuration.MONGO_URI, Configuration.MONGO_DB)
    preprocessor = CambioPreprocessor()
    service = CambioService(Configuration.BCB_API_URL, preprocessor)
    
    # Fetch and preprocess data from API
    cambios = service.fetch_and_preprocess()
    
    # Insert records into database
    for record in cambios:
        repository.insert(record)
    
    print("Data inserted successfully!")

if __name__ == "__main__":
    main()