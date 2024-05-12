# <a>*Modelagem Estática em Desenho de Software*</a>

## <a>*Introdução*</a>

A modelagem estática é uma etapa fundamental no desenvolvimento de software, fornecendo uma representação abstrata da estrutura e organização de um sistema. Ela permite aos desenvolvedores visualizar e compreender as entidades do sistema, seus relacionamentos e suas características, servindo como base sólida para a implementação e manutenção do software.

Este artefato tem como objetivo apresentar uma visão holística da modelagem estática em desenho de software, abrangendo conceitos básicos, diagramas UML relevantes e exemplos práticos.

## <a>*Metodologia*</a>

A elaboração deste artefato se baseou em diversas fontes confiáveis, incluindo livros, artigos acadêmicos, tutoriais online e materiais de cursos de engenharia de software. A metodologia de pesquisa consistiu na coleta, análise e síntese de informações relevantes sobre o tema, buscando apresentar uma abordagem abrangente e atualizada.

## <a>*O que é Modelagem Estática?*</a>

A modelagem estática foca na estrutura estável de um sistema de software, representando os elementos que o compõem e suas inter-relações, independentemente do comportamento dinâmico do sistema. Ela fornece uma visão abstrata e conceitual do software, permitindo aos desenvolvedores:

* **Visualizar e compreender a estrutura do sistema:** Através de diagramas UML, os desenvolvedores podem visualizar as entidades do sistema, seus atributos, relacionamentos e hierarquias.
* **Comunicar o design do software:** A modelagem estática facilita a comunicação entre os membros da equipe de desenvolvimento, promovendo um entendimento comum da arquitetura do sistema.
* **Analisar e identificar falhas de design:** Através da análise dos diagramas, é possível identificar falhas de design, inconsistências e potenciais problemas de implementação, permitindo a correção precoce de erros.
* **Documentar o sistema:** A modelagem estática serve como documentação formal da arquitetura do software, facilitando a compreensão e manutenção do sistema ao longo do tempo.

## <a>*Diagrama de Classes: A Base da Modelagem Estática*</a>

O diagrama de classes é a ferramenta central da modelagem estática, representando as classes do sistema, seus atributos, métodos, relacionamentos e hierarquias. Ele permite visualizar a estrutura do sistema de forma clara e concisa, servindo como base para a construção dos demais diagramas UML.

**Elementos Básicos do Diagrama de Classes:**

* **Classes:** Entidades que representam conceitos abstratos ou concretos do sistema.
* **Atributos:** Propriedades que caracterizam as classes, armazenando informações sobre seus estados.
* **Métodos:** Operações que as classes podem executar, definindo seu comportamento.
* **Relacionamentos:** Conexões entre as classes, definindo como elas interagem e colaboram entre si.
* **Herdança:** Mecanismo que permite que uma classe herde atributos e métodos de outra classe, promovendo reuso de código e organização da hierarquia de classes.

### <a>*Tipos de Relacionamentos entre Classes*</a>

Os relacionamentos entre classes definem como as entidades do sistema se conectam e interagem. Os principais tipos de relacionamentos são:

* **Associação:** Uma conexão simples entre duas classes, indicando que os objetos de uma classe podem estar relacionados aos objetos da outra classe.
* **Agregação:** Uma relação de "parte-todo", onde uma classe (parte) é composta por objetos de outra classe (todo). A parte pode existir independentemente do todo, mas sua vida útil está geralmente associada ao todo.
* **Composição:** Uma relação de "parte-todo" mais forte que a agregação, onde a parte não pode existir independentemente do todo. A destruição do todo implica na destruição das partes.
* **Dependência:** Uma relação unilateral onde uma classe depende de outra para realizar suas funções, mas não as contém nem as compõe.

### <a>*Classes Concreta, Abstrata, Sobrescrita e Sobrecarregada*</a>

* **Classe Concreta:** Uma classe que possui implementações completas para seus atributos e métodos, podendo ser instanciada em objetos.
* **Classe Abstrata:** Uma classe que define atributos e métodos, mas não possui implementações completas. Ela serve como base para classes derivadas, que herdam e implementam seus métodos abstratos.
* **Sobrescrita:** Mecanismo que permite que uma classe derivada redefina a implementação de um método herdado da classe base.
* **Sobrecarga:** Mecanismo que permite que uma classe defina métodos com o mesmo nome, mas com diferentes listas de parâmetros, permitindo diferentes comportamentos para a mesma operação.

## <a>*Diagrama de Pacotes e Componentes*</a>

* **Diagrama de Pacotes:** Representa a organização hierárquica das classes do sistema em pacotes, agrupando classes relacionadas por funcionalidade ou subsistema. Ele facilita a modularização do software, promovendo organização e reusabilidade de código.
* **Diagrama de Componentes:** Representa a visão física da arquitetura do software, mostrando como os componentes modulares do sistema se relacionam e se comunicam. Ele pode ser utilizado para modelar interfaces, dependências e bibliotecas externas utilizadas pelo sistema.

## <a>*Diagrama de Implantação*</a>

O diagrama de implantação é um tipo de diagrama UML que representa a arquitetura física de um sistema de software. Ele mostra como os componentes do sistema estão distribuídos em diferentes nós de hardware e como eles se comunicam entre si.

**Elementos Básicos do Diagrama de Implantação:**

* **Nó:** Representa um dispositivo de hardware, como um computador, servidor ou dispositivo móvel.
* **Componente:** Representa um módulo de software que é implantado em um nó.
* **Artefato:** Representa um arquivo ou outro recurso que é armazenado em um nó.
* **Dependência:** Representa uma relação de dependência entre dois componentes ou entre um componente e um artefato.
* **Conexão:** Representa uma ligação de rede entre dois nós.

**Utilização do Diagrama de Implantação:**

Os diagramas de implantação são utilizados para diversos propósitos, como:

* **Visualizar a arquitetura física do sistema:** Eles permitem visualizar como os componentes do sistema estão distribuídos em diferentes nós de hardware e como eles se comunicam entre si.
* **Planejar a infraestrutura do sistema:** Eles podem ser utilizados para planejar a infraestrutura de hardware e software necessária para o sistema.
* **Identificar e corrigir problemas de desempenho:** Através da análise do diagrama, é possível identificar e corrigir problemas de desempenho, como gargalos de rede e problemas de latência.
* **Documentar a arquitetura do sistema:** Eles servem como documentação formal da arquitetura do sistema, facilitando a compreensão e manutenção do software.

## <a>*Benefícios da Modelagem Estática*</a>

A adoção da modelagem estática no desenvolvimento de software oferece diversos benefícios, tais como:

* **Melhora na qualidade do software:** A modelagem estática permite a identificação precoce de falhas de design e inconsistências, contribuindo para a entrega de software mais robusto e confiável.
* **Facilidade de manutenção:** A documentação clara e visual proporcionada pela modelagem estática facilita a compreensão do sistema por novos desenvolvedores, tornando a manutenção e evolução do software mais eficientes.
* **Comunicação efetiva:** A modelagem estática serve como uma linguagem comum para a equipe de desenvolvimento, facilitando a comunicação e o entendimento da arquitetura do sistema.
* **Reuso de código:** Através da identificação de classes reutilizáveis e herança, a modelagem estática promove o reuso de código, reduzindo o tempo de desenvolvimento e a redundância.

## <a>*Considerações Finais*</a>

A modelagem estática é uma etapa fundamental no desenvolvimento de software orientado a objetos. Ela fornece uma base sólida para a implementação e manutenção do software, facilitando a visualização, compreensão e comunicação da estrutura do sistema. Ao adotar a modelagem estática, os desenvolvedores podem criar softwares de alta qualidade, bem organizados e fáceis de manter.


## <a>*Bibliografia*</a>

    Unified Modeling Language: https://en.wikipedia.org/wiki/Unified_Modeling_Language
    Modelagem de software com UML: https://www.devmedia.com.br/modelagem-de-software-com-uml/20140
    Modelagem de software: https://pt.wikipedia.org/wiki/Modelagem_de_software

<center>

## <a>*Histórico de Versão*</a>

| Versão |    Data    |      Descrição      |                    Autor(es)                     |             Revisor(es)             |
| :----: | :--------: | :-----------------: | :----------------------------------------------: | :---------------------------------: |
| `1.0`  | 27/04/2024 | Criação do Artefato | [João Lucas](https://github.com/VasconcelosJoao) | [Yankee](../../Subgrupos/Yankee.md) |