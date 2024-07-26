from abc import ABC, abstractmethod

class Servicos(ABC):
    @abstractmethod
    def execute(self):
        pass