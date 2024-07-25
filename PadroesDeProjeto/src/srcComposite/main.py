# Código do composite com exemplo de uso:

from .template import Template
from .agendamento_de_servicos import AgendamentoDeServicos
from .validar_certidao_ou_documento import ValidarCertidaoOuDocumento
from .baixa_de_retrovenda import BaixaDeRetrovenda
from .formulario_retrovenda import FormularioRetrovenda

if __name__ == "__main__":
    # Criando instâncias dos componentes
    agendamento = AgendamentoDeServicos()
    validar = ValidarCertidaoOuDocumento(tipoPessoa=True, numeroCertidao=12345, dataCertidao="01/01/2020")
    baixa = BaixaDeRetrovenda()
    formulario = FormularioRetrovenda(codigo_imovel=101, numero_processo="AB123", alienacao="Venda", tamanho=200, tipoDeclaracao=True, habitsNumero=456, habitsAno=2021)

    # Criando uma instância de Template e adicionando componentes
    template = Template()
    template.adicionar(agendamento)
    template.adicionar(validar)
    template.adicionar(baixa)
    template.adicionar(formulario)

    # Executando o método execute do Template, que executa os métodos execute de todos os seus filhos
    template.execute()

