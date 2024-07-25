from abc import ABC
from estadoIrregular import estadoIrregular
from estadoRegular import estadoRegular

class estadoImovel(ABC):
    def __init__(self, situacao_iptu, situacao_cartorio, situacao_metragem, situacao_proprietario):
        self.situacao_iptu = situacao_iptu
        self.situacao_cartorio = situacao_cartorio
        self.situacao_metragem = situacao_metragem
        self.situacao_proprietario = situacao_proprietario

    @classmethod
    def gera_estado(cls, situacao_iptu, situacao_cartorio, situacao_metragem, situacao_proprietario):
        estado
        if(situacao_cartorio == True and situacao_iptu == True and 
           situacao_metragem == True and situacao_proprietario == True):
            estado =  estadoRegular(situacao_iptu, situacao_cartorio, situacao_metragem, situacao_proprietario)
        else:
            estado = estadoIrregular(situacao_iptu, situacao_cartorio, situacao_metragem, situacao_proprietario)
        return estado
    def muda_estado():
        pass

    def muda_iptu(self):
        if(self.situacao_iptu == False):
            self.situacao_iptu = True
        else:
            self.situacao_iptu = False
    def muda_cartorio(self):
        if(self.situacao_cartorio == False):
            self.situacao_cartorio = True
        else:
            self.situacao_cartorio = False
    def muda_metragem(self):
        if(self.situacao_metragem == False):
            self.situacao_metragem = True
        else:
            self.situacao_metragem = False
    def muda_proprietario(self):
        if(self.situacao_proprietario == False):
            self.situacao_proprietario = True
        else:
            self.situacao_proprietario = False