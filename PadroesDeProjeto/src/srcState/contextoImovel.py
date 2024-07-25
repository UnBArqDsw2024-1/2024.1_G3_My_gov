from estadoImovel import estadoImovel

class contextoImovel:
        
    def __init__(self, imovel):
        self.imovel = imovel
        self.estado = estadoImovel.gera_estado(True, True, True, True)
    
    def muda_estado(self):
        self.estado = self.estado.muda_estado()

    def get_estado(self):
        return self.estado