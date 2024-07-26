from estadoImovel import estadoImovel

class estadoIrregular(estadoImovel):
    def __init__(self, situacao_iptu, situacao_cartorio, situacao_metragem, situacao_proprietario):
        super().__init__(situacao_iptu, situacao_cartorio, situacao_metragem, situacao_proprietario)
    
    def regularizacao_venda_direta():
        pass
    def muda_estado(self):
        if(self.situacao_cartorio == True and self.situacao_iptu == True and 
           self.situacao_metragem == True and self.situacao_proprietario == True): 
            return estadoImovel.gera_estado(self.situacao_cartorio, self.situacao_iptu, self.situacao_metragem, self.situacao_proprietario)
        else:
            return self