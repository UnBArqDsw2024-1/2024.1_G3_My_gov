from .servicos import Servicos as Componente


class ValidarCertidaoOuDocumento(Componente):
    def __init__(self, tipoPessoa: bool, numeroCertidao: int, dataCertidao: str):
        self._tipoPessoa = tipoPessoa
        self._numeroCertidao = numeroCertidao
        self._dataCertidao = dataCertidao

    def execute(self):
        print(f"Validando certidão ou documento: {self._numeroCertidao}")
