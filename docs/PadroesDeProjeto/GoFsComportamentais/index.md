# <a>*GoFs Comportamentais*</a>

## <a>*Introdução*</a>

Os padrões de design GoF Comportamentais lidam com algoritmos e atribuições de responsabilidades entre objetos. Eles se concentram na comunicação entre objetos e como eles podem alterar seu comportamento dinamicamente. Esses padrões ajudam a tornar o código mais flexível, modular e fácil de manter. Este artefato explora os principais padrões comportamentais do Gang of Four (GoF), suas características e aplicações.

## <a>*Metodologia*</a>

Este artefato foi concebido através de uma revisão da literatura sobre padrões de design, com foco nos padrões comportamentais propostos pelo Gang of Four. Foram analisados livros, artigos acadêmicos e recursos online que detalham a implementação e os benefícios desses padrões. A estrutura do documento foi organizada para facilitar a compreensão e a aplicação prática dos conceitos abordados.

## <a>*Padrões Comportamentais*</a>

### <a>*Chain of Responsibility*</a>

O padrão Chain of Responsibility evita o acoplamento do remetente de uma solicitação ao seu receptor, dando a mais de um objeto a chance de tratar a solicitação. Ele forma uma cadeia de objetos receptores e passa a solicitação ao longo dessa cadeia até que um objeto a trate.

**Exemplo de uso:** Sistemas de log que podem enviar mensagens para diferentes destinos (console, arquivo, banco de dados, etc.) dependendo da prioridade da mensagem.

### <a>*Command*</a>

O padrão Command encapsula uma solicitação como um objeto, permitindo que você parametrize clientes com diferentes solicitações, enfileire ou registre (log) solicitações e suporte operações reversíveis.

**Exemplo de uso:** Sistemas de controle remoto que podem executar diferentes comandos (ligar, desligar, aumentar volume, etc.) em diferentes dispositivos.

### <a>*Iterator*</a>

O padrão Iterator fornece uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representação subjacente.

**Exemplo de uso:** Navegação em listas, árvores e outros tipos de coleções.

### <a>*Mediator*</a>

O padrão Mediator define um objeto que encapsula como um conjunto de objetos interage. Promove o fraco acoplamento ao evitar que os objetos se refiram uns aos outros explicitamente e permite variar sua interação independentemente.

**Exemplo de uso:** Sistemas de chat onde os usuários se comunicam através de um mediador central.

### <a>*Memento*</a>

O padrão Memento captura e externaliza um estado interno de um objeto, de modo que o objeto possa ser restaurado para esse estado mais tarde, sem violar o encapsulamento.

**Exemplo de uso:** Sistemas de desfazer/refazer em editores de texto ou jogos.

### <a>*Observer*</a>

O padrão Observer define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

**Exemplo de uso:** Painéis de controle que exibem dados de diferentes fontes em tempo real.

### <a>*State*</a>

O padrão State permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado sua classe.

**Exemplo de uso:** Máquinas de estado em jogos ou sistemas de gerenciamento de pedidos.

### <a>*Strategy*</a>

O padrão Strategy define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. A estratégia permite que o algoritmo varie independentemente dos clientes que o usam.

**Exemplo de uso:** Diferentes algoritmos de ordenação em sistemas de gerenciamento de dados.

### <a>*Template Method*</a>

O padrão Template Method define o esqueleto de um algoritmo em uma operação, adiando a definição de alguns passos para subclasses. Permite que as subclasses redefinam certos passos de um algoritmo sem alterar sua estrutura.

**Exemplo de uso:** Frameworks que fornecem uma estrutura básica para aplicações, permitindo que os desenvolvedores personalizem partes específicas.

### <a>*Visitor*</a>

O padrão Visitor representa uma operação a ser realizada em elementos de uma estrutura de objeto. Permite que você defina uma nova operação sem alterar as classes dos elementos sobre os quais opera.

**Exemplo de uso:** Análise de código-fonte em ferramentas de refatoração.

## <a>*Bibliografia*</a>

    Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.

    Buschmann, F., Meunier, R., Rohnert, H., & Sommerlad, P. (1996). *Pattern-Oriented Software Architecture: A System of Patterns*. Wiley.

<Center>

## <a>*Histórico de Versão*</a>

| Versão |    Data    |       Descrição       |                    Autor(es)                     |              Revisor(es)              |
| :----: | :--------: | :-------------------: | :----------------------------------------------: | :-----------------------------------: |
| `1.0`  | 24/07/2024 | Confecção do artefato | [João Lucas](https://github.com/VasconcelosJoao) | [Whiskey](../../Subgrupos/Whiskey.md) |
