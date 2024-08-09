# <a>*Estilos e Padrões Arquiteturais*</a>

## <a>*Introdução*</a>

Nesta seção, aprofundaremos o estudo sobre Estilos e Padrões Arquiteturais, explorando suas características, benefícios e aplicações no contexto do desenvolvimento de software. Serão abordados os estilos arquiteturais de Pipes and Filters, Repositório, Orientado a Eventos e Orientado a Serviços, destacando sua relevância na construção de sistemas robustos e escaláveis.

## <a>*Pipes and Filters*</a>

O estilo arquitetural Pipes and Filters é caracterizado pela decomposição de um sistema em componentes independentes, chamados filtros, que realizam transformações específicas nos dados recebidos. Esses filtros são conectados por canais de comunicação, chamados pipes, que transportam os dados entre eles. Algumas características-chave desse estilo incluem:

- **Processamento de dados em etapas**: cada filtro realiza uma tarefa específica, permitindo a composição de processamentos complexos.
- **Reusabilidade**: os filtros podem ser reutilizados em diferentes combinações para resolver problemas distintos.
- **Paralelismo**: os filtros podem ser executados concorrentemente, aproveitando recursos de hardware.

Exemplos de aplicação incluem sistemas de processamento de imagens, compiladores e pipelines de dados em Big Data.

## <a>*Repositório*</a>

O estilo arquitetural Repositório se baseia em um componente central, chamado repositório, que gerencia o armazenamento e acesso a dados. Os demais componentes do sistema interagem com o repositório para obter, manipular e armazenar informações. Algumas características importantes:

- **Separação de concerns**: o repositório isola a lógica de acesso a dados dos demais componentes.
- **Flexibilidade de armazenamento**: o repositório pode utilizar diferentes tecnologias de armazenamento, como bancos de dados relacionais, NoSQL ou sistemas de arquivos.
- **Versionamento e controle de acesso**: o repositório pode prover funcionalidades de versionamento e controle de acesso aos dados.

Esse estilo é amplamente utilizado em sistemas de informação corporativos, como sistemas de gestão empresarial (ERP) e sistemas de gerenciamento de conteúdo (CMS).

## <a>*Visão Lógica*</a>

A visão lógica do Documento de Arquitetura de Software (DAS) descreve a decomposição do sistema em pacotes e classes, bem como os relacionamentos entre eles. Nesta aplicação, adotamos o estilo arquitetural em camadas, com as seguintes camadas principais:

- **Camada de apresentação**: responsável pela interface com o usuário e interação com a camada de aplicação.
- **Camada de aplicação**: contém a lógica de negócio e coordena as ações do sistema.
- **Camada de infraestrutura**: provê serviços de infraestrutura, como acesso a banco de dados e comunicação com sistemas externos.

Essa estrutura em camadas facilita a manutenção, evolução e reuso de componentes, além de promover a separação de concerns.

## <a>*Visão de Processo*</a>

A visão de processo descreve a dinâmica do sistema em termos de processos, threads e a interação entre eles. Para esta aplicação, adotamos um modelo baseado em processos concorrentes, onde diferentes partes do sistema podem operar simultaneamente. Os principais componentes desta visão incluem:

- **Processos Independentes**: cada módulo do sistema é implementado como um processo independente, permitindo que eles sejam escalados e gerenciados separadamente.
- **Comunicação entre Processos**: utilizamos mecanismos de comunicação como filas de mensagens e sockets para facilitar a troca de informações entre os processos.
- **Gerenciamento de Recursos**: um gerenciador de recursos é responsável por alocar e liberar recursos, garantindo que os processos tenham acesso eficiente aos dados e serviços necessários.

Esse modelo de processos concorrentes não apenas melhora a performance do sistema, mas também proporciona resiliência, já que a falha de um processo não compromete o funcionamento de todo o sistema.

## <a>*Visão de Implementação*</a>

A visão de implementação descreve como o sistema será implementado em termos de módulos de software e suas dependências. Nesta aplicação, utilizamos o padrão arquitetural Façade para simplificar a interface entre a camada de aplicação e a camada de infraestrutura. O Façade atua como um ponto de entrada único, abstraindo a complexidade da infraestrutura e fornecendo uma API simplificada para a camada de aplicação.

Esse padrão traz benefícios como:

- **Desacoplamento**: a camada de aplicação não precisa conhecer os detalhes de implementação da infraestrutura.
- **Evolução**: mudanças na infraestrutura podem ser feitas sem impactar a camada de aplicação.
- **Testabilidade**: a camada de aplicação pode ser testada de forma isolada, utilizando mocks do Façade.

## <a>*Conclusão*</a>

Neste artefato, exploramos os principais estilos e padrões arquiteturais aplicados neste projeto, destacando suas características, benefícios e aplicações. A adoção de uma arquitetura bem planejada, utilizando estilos como Pipes and Filters, Repositório e padrões como Façade, contribui para a construção de um sistema robusto, escalável e de fácil manutenção.

A especificação das visões do DAS, como a Visão Lógica, Visão de Processo e Visão de Implementação, documenta as decisões arquiteturais tomadas e facilita a comunicação entre os stakeholders. Esse processo de arquitetura de software é fundamental para o sucesso do projeto, alinhando as necessidades do negócio com as soluções técnicas.

## <a>*Bibliografia*</a>

    Buschmann, F., Meunier, R., Rohnert, H., Sommerlad, P., & Stal, M. (1996). Pattern-Oriented Software Architecture: A System of Patterns. Wiley.
    Garlan, D., & Shaw, M. (1994). An Introduction to Software Architecture. Advances in Software Engineering and Knowledge Engineering, 1.
    Hohpe, G., & Woolf, B. (2003). Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions. Addison-Wesley Professional.
    Kruchten, P. (1995). The 4+1 View Model of Architecture. IEEE Software, 12(6), 42-50.
    Medvidovic, N., & Taylor, R. N. (2000). A Classification and Comparison Framework for Software Architecture Description Languages. IEEE Transactions on Software Engineering, 26(1), 70-93.

<Center>

## <a>*Histórico de Versão*</a>

| Versão |    Data    |       Descrição       | Autor(es) | Revisor(es) |
| :----: | :--------: | :-------------------: | :-------: | :---------: |
| `1.0`  | 06/04/2024 | Confecção do artefato |   Autor   |   revisor   | 