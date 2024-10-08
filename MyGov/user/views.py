from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .models import User


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # redireciona para a página inicial após o login
        else:
            return render(request, 'user/login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'user/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')  # Redireciona para a página de login após o logout

def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password-confirm')
        if password != password_confirm:
            return render(request, 'user/cadastro.html', {'error': 'Senhas não conferem'})
        # Cria um novo usuário
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        # Faz login automaticamente após o registro
        login(request, user)
        return redirect('index')  # Redireciona para a página inicial após o registro
    return render(request, 'user/cadastro.html')

def home(request):
    return render(request, 'user/home.html')
