# <a>*Padrão do Objeto Global*</a>

## <a>*Introdução*</a>

O Padrão do Objeto Global é um padrão de design emergente que permite que um objeto seja acessível globalmente em um sistema, promovendo a reutilização e a consistência de dados. Esse padrão é particularmente útil em aplicações que requerem um único ponto de acesso a um conjunto de dados ou funcionalidades, como configurações de sistema ou serviços compartilhados. Ao implementar o Padrão do Objeto Global, os desenvolvedores podem evitar a duplicação de código e garantir que todas as partes do sistema utilizem a mesma instância de um objeto.

<a>**Benefícios do Padrão do Objeto Global:**</a>

- **Acesso Global**: Permite que um objeto seja acessado de qualquer parte do código, facilitando a interação entre diferentes componentes do sistema.
  
- **Consistência de Dados**: Garante que todos os componentes utilizem a mesma instância, evitando problemas de inconsistência.

- **Facilidade de Manutenção**: Alterações no objeto global são refletidas em toda a aplicação, simplificando a manutenção e atualização do código.

## <a>*Metodologia*</a>

Na aplicação, utilizamos o Padrão do Objeto Global para gerenciar a configuração do sistema e os serviços compartilhados. Criamos uma classe `Config` que encapsula as configurações globais e um singleton para garantir que apenas uma instância dessa classe seja criada. Essa instância é acessada em diferentes partes da aplicação, permitindo que todos os componentes leiam e modifiquem as configurações conforme necessário.

A implementação do padrão foi realizada da seguinte forma:

1. **Classe Config**: Define as propriedades e métodos para acessar e modificar as configurações globais.
2. **Singleton**: Implementa o padrão singleton para garantir que apenas uma instância da classe `Config` exista.
3. **Acesso Global**: Fornece métodos estáticos para acessar a instância global de `Config`, permitindo que qualquer parte do código interaja com as configurações.

Para ilustrar o funcionamento do padrão, foi criado um exemplo prático que demonstra a configuração e o uso de um serviço compartilhado.

## <a>*Implementação*</a>

```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key, None)

# Uso do Padrão do Objeto Global
config = Config()
config.set('database_url', 'sqlite:///:memory:')
print(config.get('database_url'))  # Acesso global à configuração
```

## <a>*Conclusão*</a>

A implementação do Padrão do Objeto Global proporcionou uma maneira eficiente de gerenciar configurações e serviços compartilhados em nossa aplicação. Através da centralização das configurações, conseguimos garantir a consistência e facilitar a manutenção do código. O padrão também promoveu uma melhor organização, permitindo que novos desenvolvedores compreendam rapidamente a estrutura do sistema.

## <a>*Bibliografia*</a>
    
    python-patterns.guide. (n.d.). The Global Object Pattern. [online] Available at: https://python-patterns.guide/python/module-globals/#the-global-object-pattern [Accessed 25 Jul. 2024].

‌

<center>

## <a>*Histórico de Versão*</a>

| Versão |    Data    |             Descrição              |                    Autor(es)                     |                 Revisor(es)                  |
| :----: | :--------: | :--------------------------------: | :----------------------------------------------: | :------------------------------------------: |
| `1.0`  | 25/07/2024 |        Criação do documento        | [João Lucas](https://github.com/VasconcelosJoao) |      [Papa](../Subgrupos/Papa.md)      |

</center>