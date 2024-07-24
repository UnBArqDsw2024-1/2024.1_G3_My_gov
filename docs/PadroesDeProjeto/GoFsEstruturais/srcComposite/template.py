from .servicos import Servicos as Componente
from typing import List

class Template(Componente):
    def __init__(self):
        self._filho: List[Componente] = []

    def adicionar(self, c: Componente):
        self._filho.append(c)

    def remove(self, c: Componente):
        self._filho.remove(c)

    def getFilho(self) -> List[Componente]:
        return self._filho

    def execute(self):
        for child in self._filho:
            child.execute()
