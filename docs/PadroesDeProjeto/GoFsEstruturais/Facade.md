
# <a>*GoFs Comportamentais*</a>

## <a>*Introdução*</a>

O padrão de projeto Facade é um padrão estrutural que fornece uma interface simplificada para um conjunto mais complexo de interfaces em um subsistema. Ele define uma interface de nível mais alto que facilita a utilização do subsistema para os clientes. Dessa forma O principal objetivo do padrão Facade é esconder a complexidade do sistema e fornecer uma interface mais simples e fácil de usar.

Além disso, o padrão Facade é especialmente útil quando um sistema é muito complexo ou difícil de entender e o cliente precisa interagir com muitas classes diferentes. Ele ajuda a reduzir a dependência entre o cliente e as classes do subsistema, promovendo uma separação mais clara das responsabilidades.

Sendo assim, no contexto do site da Terracap, o padrão Facade foi utilizado

## <a>*Metodologia*</a>

O grupo analisou vários padrões de projeto GoF, considerando suas vantagens e desvantagens no contexto do site da Terracap, um dos padrões discutido foi o facade, que possui as seguintes vantagens e desvantagens:

- Vantagens: Simplifica a integração de novos módulos e funcionalidades no site da Terracap, tornando mais fácil para os usuários finais navegarem e utilizarem as funcionalidades oferecidas, além de que reduz o acoplamento entre o cliente e os componentes do sistema. Isso melhora a modularidade e facilita a manutenção.
- Desvantagens: Como o subsistema está encapsulado no Façade, o cliente não conhece o subsistema e seus componentes, logo não pode customizar o subsistema e seus componentes diretamente. Além disso é possível esconder funcionalidades importantes se não for bem projetado.

De acordo com o livro "Design Patterns: Elements of Reusable Object-Oriented Software", quando um sistema se torna complexo com muitas classes e suas interações, os clientes do sistema podem se tornar sobrecarregados com detalhes. Sem uma interface simplificada, os clientes precisam lidar com a complexidade diretamente, o que aumenta a chance de erros e dificulta a manutenção. Como  isso se aplica ao site da Terracap, decidimos como grupo realizar um facade para contornar esse problema, expondo  métodos simples que o cliente pode usar para realizar operações necessárias, delegando chamadas apropriadas para os componentes internos do subsistema.

## <a>*Tópico 1*</a>

## <a>*Tópico 2*</a>

## <a>*Tópico N*</a>

## <a>*Bibliografia*</a>

     "Design Patterns: Elements of Reusable Object-Oriented Software" 
     DEVMEDIA. Padrão de Projeto Facade em Java. Disponível em: https://devmedia.com.br/padrao-de-projeto-facade-em-java/26476. Acesso em: 23 jul. 2024.
     PADRÕES DE PROJETO. Desvantagens do Padrão Facade. Disponível em: http://www.labies.uff.br/padroesdr/questions/3/idea/8#:~:text=Desvantagens,subsistema%20e%20seus%20componentes%20diretamente. Acesso em: 23 jul. 2024.


<Center>

## <a>*Histórico de Versão (do template)*</a>

Favor não copiar o histórico de versão dobrado, essa seção é apenas para rastrear o template de artefato

| Versão |    Data    |       Descrição       | Autor(es) | Revisor(es) |
| :----: | :--------: | :-------------------: | :-------: | :---------: |
| `1.0`  | 24/07/2024 | Confecção do artefato |   Foxtrot   |   Whiskey   |
