# <a>*Diagrama de Sequência*</a>

## Introdução

Esse artefato ilustra por meio de diagramas de sequência, as chamadas de processos e métodos em determinados funcionalidades baseadas no site da Terracap. As funcionalidades selecionadas para representação foram, cadastro, login, e solicitação de declaração de retrovenda.

## Metodologia

Para a elaboração desse artefato, foi utilizado o material didático em slides, e o material complementar disponibilizado pela professora Milene Serrano. Para a criação do diagrama, foi utilizada a ferramenta LucidChart.

## O que é um Diagrama de Sequência?

Um Diagrama de Sequência é uma representação gráfica que ilustra o fluxo de chamadas de processos/métodos em um sistema. Ele mostra o momento que as chamadas são realizadas e em que sequência.

## <a>*Principais Elementos de um Diagrama de Sequência*</a>

##### <a>*1. LifeLine*</a>

Rpresentados por retangulos grandes com a identificação de uma determinado objeto, logo a abaixo do retângulo temos uma linha que representa o "tempo de vida" de determinada entidade durante o fluxo da atividade.

##### <a>*2. Execution specification*</a>

Representado por retangulos longos e finos, ilustram o tempo em que determinado método leva para leva para ser executado e retornar uma resposta.

##### <a>*3. Synchronous/asynchronous message*</a>

Representados por setas de pontas preenchidas/vazias, respectivamente. Identificam quando um método é acionado e quando é feito o retorno de uma resposta do método.

##### <a>*4. Interaction use*</a>

Representado por um retângulo branco com uma marcação na ponta. Representa alguma possível interação com o usuário, seja mostrar um dado ou um input.

##### <a>*5. Duration constraint*</a>

Representado por uma seta vertical com duas setas nas pontas. Identifica o tempo entre duas "Execution specification" diferentes.

##### <a>*6. Object creation message*</a>

Mesma representação de uma "Synchronous/asynchronous message", contudo com um texto em cima que vai descrever que um método contrutor de entidade está sendo chamado.

##### <a>*6. Destruction object*</a>

Representado por um "X", demarcar o final de uma "LifeLine" de determinada entidade, sendo encerrada e só poderá ser chamada novamente se alguma método contrutor da entidade for chamado antes. 

# <a>*Fluxos*</a>

## <a>*Cadastro*</a>

![Diagrama de atividades do cadastro](../../Assets/DiagramaSequencia/cadastro_sequencia.png)

## <a>*Login*</a>

![Diagrama de atividades do login](../../Assets/DiagramaSequencia/login_sequencia.png)

## <a>*Solicitar Declaração de Retrovenda*</a>

![Diagrama de atividades da declaração da retrovenda](../../Assets/DiagramaSequencia/solicitar_dec_sequencia.png)

## <a>*Vantagens do Diagrama de Sequência</a>

- Fluxo de Controle: Proporciona uma visão clara do fluxo de processos de determinada atividade.
- Identificação de Condições: Ajuda a identificar, gargalos e depências de processos no fluxo.

## <a>*Quando Usar um Diagrama de Sequência?*</a>

- Desenvolvimento de Software: Mapear a comunicação entreos diversos componentes do sistema, principalmente usas dependências e paralelismo.
- Modelagem de Processos de Negócio: Estabelecer um fluxo de prioridade e dependência com maior eficiência.
- Documentação de Sistemas: Contribui para criar uma documentação clara e compreensível dos fluxos de trabalho.

## Bibliografia

[1] SERRANO. MILENE, AULA - MODELAGEM UML DIN MICA, 2024. Disponível em: <https://aprender3.unb.br/pluginfile.php/2790248/mod_label/intro/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20Modelagem%20UML%20Din%C3%A2mica%20-%20Profa.%20Milene.pdf>

[2] LUCIDCHART, UML Activity Diagram Tutorial. Disponível em: <https://www.lucidchart.com/pages/uml-activity-diagram>


<center>

## <a>*<a>*Histórico de Versão*</a>*</a>

| Versão |    Data    |             Descrição             |               Autor(es)               |                   Revisor(es)                    |
| :----: | :--------: | :-------------------------------: | :-----------------------------------: | :----------------------------------------------: |
| `1.0`  | 07/07/2024 |       Criação do documento        | [Foxtrot](../../Subgrupos/Foxtrot.md) | [João Lucas](https://github.com/VasconcelosJoao) |

</center>
