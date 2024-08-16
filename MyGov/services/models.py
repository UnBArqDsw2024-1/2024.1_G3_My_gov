from django.db import models
from user.models import User

# Model Endereco
class Endereco(models.Model):
    complemento = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='enderecos', on_delete=models.CASCADE)

    def validate_registration_data(self):
        pass  # implementar lógica

    def update_profile(self, name, address, cep, date_of_birth):
        pass  # implementar lógica

# Model Information -> TALVEZ SEJA MELHOR COMO UMA VIEW
class Information(models.Model):
    numero_processo = models.CharField(max_length=50)
    tamanho_imovel = models.CharField(max_length=50)
    numero_habite_se = models.IntegerField()
    data_expedicao = models.DateField()
    tipo_declaracao = models.BooleanField(default=False)
    tipo_proprietario = models.CharField(max_length=50)
    ano_habite_se = models.IntegerField()
    alienacao = models.CharField(max_length=255)

    def show_information(self):
        pass  # implementar lógica

    def edit_information(self):
        pass  # implementar lógica


# Model DeclaracaoRetroVenda herdando Content
class DeclaracaoRetroVenda(models.Model):
    regiao = models.CharField(max_length=100)
    codigo_imovel = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    information = models.OneToOneField(Information, on_delete=models.CASCADE)

    def visualizar_mapa(self):
        pass  # implementar lógica

    def solicitar_por_regiao(self, regiao):
        pass  # implementar lógica

    def solicitar_por_codigo(self, codigo_imovel):
        pass  # implementar lógica
