from .servicos import Servicos as Componente

class FormularioRetrovenda(Componente):
    def __init__(self, codigo_imovel: int, numero_processo: str, alienacao: str, tamanho: int, tipoDeclaracao: bool, habitsNumero: int, habitsAno: int):
        self._codigo_imovel = codigo_imovel
        self._numero_processo = numero_processo
        self._alienacao = alienacao
        self._tamanho = tamanho
        self._tipoDeclaracao = tipoDeclaracao
        self._habitseNumero = habitsNumero
        self._habitseAno = habitsAno

    def execute(self):
        print(f"Executando formulário de retrovenda para imóvel: {self._codigo_imovel}")
