from django.shortcuts import render
from .models import DeclaracaoRetroVenda

def index(request):
    context = {
        'message': "Hello, world. You're at the services index."
    }
    return render(request, 'index.html', context)

def retrovenda(request):
    if request.method == 'POST':
        codigo_imovel = request.POST.get('codigo_imovel')
        declaracao = DeclaracaoRetroVenda.objects.filter(codigo_imovel=codigo_imovel)
        if declaracao:
            return render(request, 'info.html', {'codigo_imovel': codigo_imovel, 'declaracao': declaracao[0], 'endereco': declaracao[0].endereco})
        return render(request, 'retrovenda.html', {'codigo_imovel': codigo_imovel})
    return render(request, 'retrovenda.html')