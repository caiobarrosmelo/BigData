class Cambio:
    
    def __init__(self, paridade_compra, paridade_venda, cotacao_compra,
                 cotacao_venda, data_cotacao, tipo_boletim):
        self.paridade_compra = paridade_compra
        self.paridade_venda = paridade_venda
        self.cotacao_compra = cotacao_compra
        self.cotacao_venda = cotacao_venda
        self.data_cotacao = data_cotacao
        self.tipo_boletim = tipo_boletim    
    
    def to_dict(self):
        return{
            "paridade_compra": self.paridade_compra,
            "paridade_venda": self.paridade_venda,
            "cotacao_compra": self.cotacao_compra,
            "cotacao_venda": self.cotacao_venda,
            "data_cotacao": self.data_cotacao,
            "tipo_boletim": self.tipo_boletim
        }