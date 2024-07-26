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