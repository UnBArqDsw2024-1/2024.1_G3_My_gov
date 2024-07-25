# <a> *Composite* </a>

## <a>*Introdução*</a>

O padrão Composite é um padrão de projeto estrutural que permite que objetos sejam compostos em estruturas de árvore, possibilitando que os clientes tratem tanto os objetos individuais quanto as composições de objetos de forma uniforme. Este padrão é especialmente útil em situações onde é necessário representar hierarquias de objetos, como em sistemas de arquivos ou interfaces gráficas, onde componentes podem ser agrupados e manipulados de maneira consistente.

A principal vantagem do padrão Composite é a simplificação do código que manipula estruturas complexas, permitindo que operações sejam realizadas em grupos de objetos sem a necessidade de diferenciar entre objetos simples e compostos. Isso resulta em um design mais flexível e extensível, facilitando a adição de novos tipos de componentes sem a necessidade de modificar o código existente.

Neste artefato, o subgrupo [Yankee](../../Subgrupos/Yankee.md) explora a aplicação do padrão Composite em um contexto específico, abordando a problemática da baixa de retrovenda e propondo uma solução que utiliza a composição de serviços para facilitar o agendamento, validação de documentos e o preenchimento de formulários. A implementação em Python é apresentada, juntamente com um diagrama UML que ilustra a estrutura do sistema.

## <a>*Metodologia*</a>

Para elaboração do artefato o subgrupo [Yankee](../../Subgrupos/Yankee.md) realizou reuniões e discussões entre os dias 17/07 até 24/07 sendo realizada a entrega no dia 25/07. Nos primeiro dia (17) foi realizado um estudo sobre o padrão e escolhido uma problemática que ele poderia resolver, no qual optamos por fazer uma adaptação do Composite com base no [Prótipo](../../Base/DesignSprint/prototipo.md) e no [Diagrama de Classe](../../Modelagem/ModelagemEstatica/DiagramaDeClasses.md). Depois entre os dias 22 a 24, foi realizada a escrita dos textos de introdução, problemática e de solução, além da construção do diagrama UML. Por fim no dia 24 foi dedicado para a implementação do UML em código Python.


## <a>*Problema e Solução*</a>

### <a>*Problema*</a>

O contexto de Baixa de Retrovenda foi selecionado com base nas inspirações acima, identificando o problema ao solicitar uma retrovenda e o respectivo formulário associado a ela, além das funcionalidades de Solicitar Agendamendo de Serviços e Validar Certidão ou Documento. 

### <a>*Solução*</a>

A seguir são apresentados o diagrama UML e ocódigo relativo à problemática em questão. 

## <a>*UML*</a>

<center>
 <a id='ref2'>Figura 1 - Diagrama UML </a>

<br> ![alt text](../../Assets/DiagramaUML/GoFComposite.png) <br>

<font>Fonte: <a>[Yankee](../../Subgrupos/Yankee.md)</a>, 2024</font>

</center>

O diagrama foi construído baseado na estrutura apresentada em sala de aula e com o auxílio do site [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/observer).


## <a>*Código*</a>

* Classe Servicos (servicos.py) 

Esta é uma classe abstrata base que define a interface para todos os serviços. Ela utiliza o módulo abc para definir métodos abstratos.

```python
from abc import ABC, abstractmethod

class Servicos(ABC):
    @abstractmethod
    def execute(self):
        pass

```

* Classe Template (template.py)

Implementa a interface de composição de serviços.

```python
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
            
```

* Classe ValidarCertidaoOuDocumento (validar_certidao_ou_documento.py)

Valida certidões ou documentos específicos.

```python
from .servicos import Servicos as Componente


class ValidarCertidaoOuDocumento(Componente):
    def __init__(self, tipoPessoa: bool, numeroCertidao: int, dataCertidao: str):
        self._tipoPessoa = tipoPessoa
        self._numeroCertidao = numeroCertidao
        self._dataCertidao = dataCertidao

    def execute(self):
        print(f"Validando certidão ou documento: {self._numeroCertidao}")
```

* Classe AgendamentoDeServico (agendamento_de_servicos.py)

 Implementa a lógica de agendamento de serviços.

```python
from .servicos import Servicos as Componente
from typing import List

class AgendamentoDeServicos(Componente):
    def __init__(self):
        self._agendamento: List = []

    def execute(self):
        print("Executando agendamento de serviços")
```

* Classe BaixaDeRetrovenda (baixa_de_retrovenda.py)

Implementa a lógica de baixa de retrovenda.

```python
from .servicos import Servicos as Componente
from typing import List


class BaixaDeRetrovenda(Componente):
    def __init__(self):
        self._selecionarRegiao: List = []
        self._selecionarSetor: List = []
        self._selecionarImovel: List = []

    def execute(self):
        print("Executando baixa de retrovenda")
```

* Classe FormularioRetrovenda (formulario_retrovenda.py)

Implementa a lógica de preenchimento do formulário de retrovenda.

```python
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
```

## <a>*Resultado de exemplo*</a>

* Arquivo de teste (main.py)
```python
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
```

* Saída
```
Executando agendamento de serviços
Validando certidão ou documento: 12345
Executando baixa de retrovenda
Executando formulário de retrovenda para imóvel: 101
```

## <a>*Bibliografia*</a>

    GAMMA, Eric, et al. **Design Patterns: Elements of Reusable Object-Oriented Software.** 1rd ed. Indianapolis: Pearson Education, 1994.

    [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/composite).


## <a>*Histórico de Versão*</a>

<Center>

Favor não copiar o histórico de versão dobrado, essa seção é apenas para rastrear o template de artefato

| Versão |    Data    |       Descrição       | Autor(es) | Revisor(es) |
| :----: | :--------: | :-------------------: | :-------: | :---------: |
| `1.0`  | 22/07/2024 | Confecção do artefato |   [Yankee](../../Subgrupos/Yankee.md)  |   [Whiskey](../../Subgrupos/Whiskey.md)   |
| `2.0`  | 24/07/2024 | Finalização diagrama e implementação |   [Yankee](../../Subgrupos/Yankee.md)  |   [Whiskey](../../Subgrupos/Whiskey.md)   |

</Center>