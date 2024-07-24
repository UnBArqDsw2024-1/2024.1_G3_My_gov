# <a>*GoFs Criacionais*</a>

## <a>*Introdução*</a>

O padrão de design Gof Criacional refere-se a um conjunto de técnicas e soluções que facilitam a criação de objetos em programação orientada a objetos. Esses padrões são fundamentais para a flexibilidade e a manutenção do código, permitindo que os desenvolvedores criem instâncias de classes de maneira eficiente e controlada. Este artefato explora os principais padrões criacionais do Gang of Four (GoF), suas características e aplicações.

## <a>*Metodologia*</a>

Este artefato foi concebido através de uma revisão da literatura sobre padrões de design, com foco nos padrões criacionais propostos pelo Gang of Four. Foram analisados livros, artigos acadêmicos e recursos online que detalham a implementação e os benefícios desses padrões. A estrutura do documento foi organizada para facilitar a compreensão e a aplicação prática dos conceitos abordados.

## <a>*Padrões Criacionais*<a>

### <a>*Singleton*</a>

O padrão Singleton garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a essa instância. É amplamente utilizado em situações onde um único objeto é necessário para coordenar ações em todo o sistema.

**Exemplo de uso:** Gerenciadores de configuração, onde uma única instância deve controlar as configurações da aplicação.

### <a>*Factory Method*</a>

O Factory Method define uma interface para criar um objeto, mas permite que as subclasses decidam qual classe instanciar. Esse padrão promove a desacoplamento entre a criação de objetos e seu uso.

**Exemplo de uso:** Sistemas que precisam de diferentes tipos de produtos, como um sistema de gerenciamento de pedidos que pode criar diferentes tipos de pedidos (online, presencial, etc.).

### <a>*Abstract Factory*</a>

O padrão Abstract Factory fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. Isso é útil quando o sistema deve ser independente de como seus produtos são criados.

**Exemplo de uso:** Interfaces gráficas que precisam de diferentes estilos de botões e janelas, dependendo do sistema operacional.

### <a>*Builder*</a>

O padrão Builder separa a construção de um objeto complexo da sua representação, permitindo que o mesmo processo de construção crie diferentes representações. Isso é especialmente útil quando um objeto possui muitas partes ou configurações.

**Exemplo de uso:** Construção de um documento complexo, como um relatório, onde diferentes seções podem ser adicionadas de forma flexível.

### <a>*Prototype*</a>

O padrão Prototype permite que um objeto crie cópias de si mesmo, facilitando a clonagem de objetos complexos sem depender de suas classes concretas. Este padrão é útil quando a criação de um novo objeto é cara em termos de recursos.

**Exemplo de uso:** Jogos onde os personagens podem ser duplicados ou modificados a partir de um modelo existente.

## <a>*Bibliografia*</a>

    Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.

    Buschmann, F., Meunier, R., Rohnert, H., & Sommerlad, P. (1996). *Pattern-Oriented Software Architecture: A System of Patterns*. Wiley.

<Center>

## <a>*Histórico de Versão (do template)*</a>

Favor não copiar o histórico de versão dobrado, essa seção é apenas para rastrear o template de artefato

| Versão |    Data    |       Descrição       |                    Autor(es)                     | Revisor(es) |
| :----: | :--------: | :-------------------: | :----------------------------------------------: | :---------: |
| `1.0`  | 23/07/2024 | Confecção do artefato | [João Lucas](https://github.com/VasconcelosJoao) |   Revisor   |