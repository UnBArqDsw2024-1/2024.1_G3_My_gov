# <a>*GoFs Criacionais*</a>

## <a>*Introdução*</a>

Os padrões de projeto GoF (Gang of Four) são soluções testadas e comprovadas para problemas comuns de design de software. Existem três categorias principais de padrões de projeto: criacionais, estruturais e comportamentais. Os padrões criacionais lidam com a criação de objetos, fornecendo diretrizes para criar objetos de maneira adequada e flexível. Eles ajudam a abstrair o processo de instanciar objetos, promovendo a reutilização de código e a flexibilidade.

## <a>*Metodologia*</a>

??

## <a>*GoFs Criacional Factory Method*</a>

O Factory Method é um padrão de projeto criacional que define uma interface para criar um objeto, mas permite que as subclasses alterem o tipo de objeto que será criado. Ele promove o princípio aberto/fechado, permitindo a extensão do código sem modificá-lo. O Factory Method é útil quando a classe não pode antecipar a classe dos objetos que deve criar ou quando uma classe deseja que suas subclasses especifiquem esses objetos.

Beneficios do factory Method:

- Desacoplamento: A lógica de criação de documentos é desacoplada da lógica de negócios.
- Extensibilidade: Adicionar novos tipos de documentos é fácil e não requer mudanças nas partes existentes do sistema.
- Manutenibilidade: Centralizar a lógica de criação de documentos facilita a manutenção e o entendimento do código.


## <a>*Utilização no TerraCap*</a>

Na aplicação, utilizamos o padrão de projeto Factory Method para gerenciar a criação de diferentes tipos de documentos, como declarações de retrovenda e boletos. Centralizamos a lógica de criação de documentos na classe abstrata Documento Factory, que define um método Create_Documento a ser implementado por suas subclasses concretas, Declaracao_RetrovendaFactory e Boleto_Factory. Essas fábricas concretas são responsáveis por instanciar os documentos específicos (declaração de retrovenda e boleto), cada um com seus atributos particulares. Esse padrão nos permite adicionar novos tipos de documentos conforme necessidade futura, de maneira flexível mantendo a coesão e a organização do código, além de facilitar a manutenção e a extensão da aplicação.

## <a>*Modelagem do Factory Method*</a>

![Diagrama Criacional Factory Method](docs/Assets/GoFCriacional/DiagramaPacotes.png)


## <a>*Aplicação do Factory Method*</a>

codigo

## <a>*Conclusão*</a>

Com o uso do padrão de projeto Factory Method, conseguimos organizar e gerenciar eficientemente a criação de diferentes tipos de documentos na aplicação TerraCap. Este padrão oferece vários benefícios, como desacoplamento, extensibilidade e manutenibilidade, ao centralizar a lógica de criação de documentos e delegar a responsabilidade de instanciar objetos específicos para subclasses concretas. Dessa forma, a aplicação se torna mais flexível e adaptável a mudanças futuras, permitindo a adição de novos tipos de documentos sem a necessidade de modificar o código existente. A implementação do Factory Method, portanto, contribui significativamente para a manutenção da coesão e da organização do código, facilitando o desenvolvimento e a extensão contínua da aplicação.


## <a>*Bibliografia*</a>

    SERRANO. MILENE, AULA - GoFs Criacionais, Universidade de Brasília, 2024

    Gamma, Erich, Richard Helm, Ralph Johnson, e John Vlissides.Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.

<Center>

## <a>*Histórico de Versão*</a>


| Versão |    Data    |       Descrição       | Autor(es) | Revisor(es) |
| :----: | :--------: | :-------------------: | :-------: | :---------: |
| `1.0`  | 23/07/2024 | Confecção do artefato |   Papas   |   revisor   |
