# <a>Documento de Reutilização de Software</a>

## <a>Introdução</a>

A reutilização de software é uma prática essencial no desenvolvimento de sistemas, que envolve a utilização de componentes, módulos ou trechos de código já existentes. Essa abordagem visa aumentar a eficiência e a produtividade, reduzindo o tempo e o custo de desenvolvimento, além de evitar a duplicação de esforços. A reutilização não apenas promove a padronização e a qualidade do software, mas também se torna crucial diante da crescente complexidade dos sistemas modernos. Com a evolução dos processos de desenvolvimento, a reutilização de software se consolidou como uma estratégia vital para enfrentar os desafios de inovação e manutenção contínua, permitindo que as equipes se concentrem em novas funcionalidades em vez de reinventar a roda.

## <a>Metodologia</a>

A metodologia adotada para o projeto inclui a aplicação de práticas ágeis, que favorecem a colaboração e a adaptação contínua. Utilizamos ferramentas de versionamento como Git para gerenciar o código e acompanhar as contribuições de cada membro do subgrupo. O vídeo demonstrativo da metodologia será disponibilizado a seguir para melhor compreensão do processo.

<center>

<iframe width="800" height="400" src="https://www.youtube-nocookie.com/embed/39Ghah-Dyik" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</center>

## <a>Ferramentas</a>

### <a>Backend</a>

- *Python*: Escolhemos Python pela sua simplicidade e legibilidade, que facilitam tanto o desenvolvimento quanto a manutenção do código. A linguagem também oferece uma ampla gama de bibliotecas e frameworks que agilizam a implementação de funcionalidades.
  
  - *Django*: Utilizamos Django por sua robustez e pela capacidade de facilitar o desenvolvimento de aplicações web, permitindo a criação rápida de protótipos e a integração de funcionalidades complexas com segurança.

### <a>Frontend</a>

- *JavaScript*: Optamos por JavaScript, que é a linguagem padrão para desenvolvimento web. Utilizamos frameworks como React para criar interfaces dinâmicas e responsivas, melhorando a experiência do usuário.

### <a>Banco de dados</a>

- *SQLite*: A escolha do SQLite se deve à sua leveza e simplicidade, sendo ideal para aplicações que não requerem um sistema de gerenciamento de banco de dados robusto. O SQLite permite que a aplicação armazene dados em um único arquivo, facilitando a portabilidade e o gerenciamento.

## Pontos de Reutilização

	- Serviços

Os modelos estendem models.Model, o que significa que eles herdam toda a infraestrutura fornecida pelo Django para persistência de dados, validação e migração de banco de dados. Isso permite que você reutilize funcionalidades como validação de campos, operações CRUD (Create, Read, Update, Delete) e integração com o ORM (Object-Relational Mapping) do Django, sem precisar implementar essas funcionalidades manualmente. Além disso, o Django fornece campos predefinidos (como CharField, DateField, BooleanField) que estamos utilizando. Esses campos são altamente reutilizáveis e personalizáveis, o que facilita o desenvolvimento de modelos de dados robustos e flexíveis. 

Reutilização futura:
No futuro, o sistema da Terracap pode precisar de novas funcionalidades, como a integração com outros sistemas ou a adição de novos tipos de declarações ou documentos. A modularidade dos modelos atuais permitirá que novas funcionalidades sejam adicionadas sem grandes mudanças na estrutura existente.

- Usuário

Pontos de Reutilização de Software no modelos de usuários:
Extensão de AbstractUser:
Essa extensão aproveita e reutiliza uma classe robusta do Django, que já contém toda a infraestrutura necessária para autenticação e gerenciamento de usuários. Isso evita a necessidade de reescrever funcionalidades complexas, como hash de senhas, permissões, e grupos de usuários, e permite se concentrar em adicionar funcionalidades específicas ao nosso projeto.

Reutilização futura:
O modelo utilizado no User permite que esse possa ser reutilizado em diferentes partes da aplicação que necessitam de informações específicas sobre o usuário. Essa abordagem centralizou os dados do usuário em um único modelo, o que facilita a manutenção e expansão futura. 



## <a>Justificativa</a>

Escolhemos essas funcionalidades para reutilização devido à sua relevância e aplicabilidade em diversos projetos. A funcionalidade de login é um componente crítico em qualquer sistema que requer autenticação, enquanto a funcionalidade de cadastro é fundamental para a criação de novos usuários. Ambas as funcionalidades são frequentemente necessárias em uma variedade de aplicações, o que justifica sua reutilização.

## <a>Conclusões</a>

A reutilização de software não só economiza tempo e recursos, mas também melhora a qualidade do produto final. Ao adotar práticas de reutilização, nossa equipe pôde focar em aspectos inovadores do projeto, enquanto se beneficiava de soluções já testadas e validadas. Essa abordagem não apenas aumenta a eficiência do desenvolvimento, mas também contribui para a criação de um código mais limpo e sustentável.

## <a>Referências</a>

    A reutilização de software e suas aplicações. Blog Casa do Desenvolvedor. (https://blog.casadodesenvolvedor.com.br/reutilizacao-de-software/)
    Reutilização de Software na Engenharia de Software: Conceitos e práticas. LinkedIn. (https://pt.linkedin.com/pulse/reutiliza%C3%A7%C3%A3o-de-software-na-engenharia-conceitos-e-gomes-rocha-odxxf)
    Diretrizes para Reutilização de Software. CIn UFPE. (https://www.cin.ufpe.br/~rls2/processo_tg/Metodologia%20S%26B/guidances/guidelines/software_reuse_6BA25ECC.html)
    Análise da Reutilização de Software em Projetos de Desenvolvimento. (https://www.enacomp.com.br/2011/anais/trabalhos-aprovados/pdf/enacomp2011_submission_43.pdf)
    Reuso de Software: Uma Abordagem Prática. (https://www.inf.ufpr.br/silvia/ES/reuso/reusoAl.pdf)


<Center>

## <a><a>*Histórico de Versão</a>*</a>

| Versão |    Data    |       Descrição       | Autor(es) | Revisor(es) |
| :----: | :--------: | :-------------------: | :-------: | :---------: |
|  1.0   | 06/04/2024 | Confecção do artefato |   Autor   |   revisor   |