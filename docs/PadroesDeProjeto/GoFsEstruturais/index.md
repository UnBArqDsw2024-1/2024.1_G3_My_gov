# <a>*GoFs Estruturais*</a>

## <a>*Introdução*</a>

Os padrões de design GoF Estruturais tratam da composição de classes e objetos para formar estruturas maiores. Eles ajudam a garantir que, ao compor objetos, o sistema permaneça flexível e eficiente. Esses padrões são essenciais para a construção de sistemas que são fáceis de entender e manter. Este artefato explora os principais padrões estruturais do Gang of Four (GoF), suas características e aplicações.

## <a>*Metodologia*</a>

Este artefato foi elaborado através de uma revisão da literatura sobre padrões de design, com foco nos padrões estruturais propostos pelo Gang of Four. Foram analisados livros, artigos acadêmicos e recursos online que detalham a implementação e os benefícios desses padrões. A estrutura do documento foi organizada para facilitar a compreensão e a aplicação prática dos conceitos abordados.

## <a>*Padrões Estruturais*</a>

### <a>*Adapter*</a>

O padrão Adapter permite que interfaces incompatíveis trabalhem juntas. Ele atua como um intermediário que converte a interface de uma classe em outra interface que os clientes esperam.

**Exemplo de uso:** Integração de uma nova biblioteca de terceiros em um sistema existente que requer uma interface diferente.

### <a>*Bridge*</a>

O padrão Bridge desacopla uma abstração da sua implementação, permitindo que ambas variem independentemente. Isso é útil quando você deseja evitar a explosão de subclasses.

**Exemplo de uso:** Sistemas gráficos onde diferentes formas (círculos, quadrados) podem ser renderizadas em diferentes plataformas (Windows, Linux).

### <a>*Composite*</a>

O padrão Composite permite que você componha objetos em estruturas de árvore para representar hierarquias parte-todo. Ele permite que os clientes tratem objetos individuais e composições de maneira uniforme.

**Exemplo de uso:** Estruturas de diretórios em sistemas de arquivos, onde arquivos e pastas podem ser tratados de forma semelhante.

### <a>*Decorator*</a>

O padrão Decorator permite adicionar funcionalidade a um objeto dinamicamente, sem alterar sua estrutura. Isso é feito através de uma classe que "decorates" (adiciona) funcionalidade ao objeto original.

**Exemplo de uso:** Sistemas de gerenciamento de janelas onde diferentes estilos ou funcionalidades podem ser adicionados a uma janela sem modificar sua classe base.

### <a>*Facade*</a>

O padrão Facade fornece uma interface simplificada para um conjunto de interfaces em um subsistema, facilitando o uso do subsistema para o cliente.

**Exemplo de uso:** APIs complexas onde uma interface simples é necessária para facilitar a interação com o sistema.

### <a>*Flyweight*</a>

O padrão Flyweight é usado para minimizar o uso de memória ao compartilhar o máximo possível de dados entre objetos semelhantes. É especialmente útil quando muitos objetos são criados que têm características comuns.

**Exemplo de uso:** Sistemas de jogos onde muitos objetos (como árvores ou inimigos) compartilham características comuns e podem ser representados com menos dados.

### <a>*Proxy*</a>

O padrão Proxy fornece um substituto ou representante de outro objeto para controlar o acesso a ele. Isso pode ser útil em situações onde o objeto real é caro para criar ou acessar.

**Exemplo de uso:** Controle de acesso a objetos que requerem autenticação ou autorização, como serviços de banco de dados ou APIs.

## <a>*Bibliografia*</a>

    Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.

    Buschmann, F., Meunier, R., Rohnert, H., & Sommerlad, P. (1996). *Pattern-Oriented Software Architecture: A System of Patterns*. Wiley.

<Center>

## <a>*Histórico de Versão*</a>

| Versão |    Data    |       Descrição       |                    Autor(es)                     |              Revisor(es)              |
| :----: | :--------: | :-------------------: | :----------------------------------------------: | :-----------------------------------: |
| `1.0`  | 24/07/2024 | Confecção do artefato | [João Lucas](https://github.com/VasconcelosJoao) | [Foxtrot](../../Subgrupos/Foxtrot.md) |