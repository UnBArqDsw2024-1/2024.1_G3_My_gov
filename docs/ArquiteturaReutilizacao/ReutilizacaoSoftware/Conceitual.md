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

## <a>Pontos Candidatos à Reutilização</a>

### <a>Funcionalidade de Login</a>

A funcionalidade de login do sistema Terracap permite que os usuários acessem o portal mediante a autenticação de suas credenciais. Após a validação, o sistema concede acesso aos serviços e informações restritas, garantindo a segurança e a privacidade dos dados dos usuários.

### <a>Funcionalidade de Cadastro</a>

Esta funcionalidade permite que novos usuários se registrem no sistema, coletando informações essenciais e armazenando-as de maneira segura. A reutilização deste módulo pode ser aplicada em diferentes contextos, como em sistemas de e-commerce ou plataformas educacionais.

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