import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao path
# Sobe até a pasta BigData (raiz do projeto)
root_path = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_path))

from AtividadePratica4.app.models.cambio import Cambio

#Realiza etapas de limpeza, validação e conversão
class CambioPreprocessor:
    def process(self, data):
        # Valida e converte os campos conforme necessário
        paridade_compra = int(data.get("paridadeCompra", 0))
        paridade_venda = int(data.get("paridadeVenda", 0))
        cotacao_compra = int(data.get("cotacaoCompra", 0))
        cotacao_venda = int(data.get("cotacaoVenda", 0))
        data_cotacao = data.get("dataHoraCotacao")
        tipo_boletim = data.get("tipoBoletim")
        
        return Cambio(  # ← CORRIGI AQUI: deve retornar Cambio, não CambioPreprocessor
            paridade_compra, paridade_venda, cotacao_compra, 
            cotacao_venda, data_cotacao, tipo_boletim
        )
        
        import sys
from pathlib import Path


# Obtém o caminho raiz do projeto subindo 4 níveis na hierarquia de diretórios
# Partindo de: BigData/AtividadePratica4/app/preprocessors/cambio_preprocessor.py
# Chegando em: BigData/ (raiz do projeto)
# root_path = Path(__file__).parent.parent.parent.parent

# Debug: exibe o caminho completo do arquivo atual sendo executado
# print(f"Caminho atual do arquivo: {Path(__file__)}")

# Debug: exibe o caminho raiz calculado (BigData/)
# print(f"Root path calculado: {root_path}")

# Debug: verifica se o diretório raiz existe no sistema de arquivos
# print(f"Root path existe? {root_path.exists()}")

# Adiciona o caminho raiz ao início da lista de caminhos de busca de módulos do Python
# Isso permite que o Python encontre e importe módulos a partir da raiz do projeto
# sys.path.insert(0, str(root_path))