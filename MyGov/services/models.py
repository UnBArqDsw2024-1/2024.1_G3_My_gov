from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Model User extendendo AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    tipo_pessoa = models.CharField(max_length=50)
    rg = models.CharField(max_length=20)
    orgao_emissor = models.CharField(max_length=50)
    uf_emissor = models.CharField(max_length=2)
    estrangeiro = models.BooleanField(default=False)
    estado_civil = models.CharField(max_length=50)
    ddd = models.IntegerField(null=True, blank=True)
    celular = models.IntegerField(null=True, blank=True)

    def view_content(self, request):
        # Função para exibir conteúdo após login
        if request.user.is_authenticated:
            return render(request, 'user/content.html', {'user': request.user})
        else:
            return redirect('login')  # redireciona para a página de login se não autenticado

    def register(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            # Cria um novo usuário
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            # Faz login automaticamente após o registro
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o registro
        return render(request, 'user/register.html')

    def logout_user(self, request):
        # Função para logout do usuário
        logout(request)
        return redirect('home')  # Redireciona para a página inicial após logout


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
