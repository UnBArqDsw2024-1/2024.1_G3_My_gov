from .servicos import Servicos as Componente
from typing import List

class AgendamentoDeServicos(Componente):
    def __init__(self):
        self._agendamento: List = []

    def execute(self):
        print("Executando agendamento de serviços")
