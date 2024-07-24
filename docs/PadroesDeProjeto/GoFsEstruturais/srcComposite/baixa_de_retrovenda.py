from .servicos import Servicos as Componente
from typing import List


class BaixaDeRetrovenda(Componente):
    def __init__(self):
        self._selecionarRegiao: List = []
        self._selecionarSetor: List = []
        self._selecionarImovel: List = []

    def execute(self):
        print("Executando baixa de retrovenda")
