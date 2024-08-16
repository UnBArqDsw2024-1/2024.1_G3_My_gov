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
        if codigo_imovel == None:
            endereco = request.POST.get('endereco')
            declaracao = DeclaracaoRetroVenda.objects.filter(endereco=endereco)
            if declaracao:
                return render(request, 'info.html', {'declaracao': declaracao[0], 'endereco': endereco})

            return render(request, 'info.html', {'declaracao': None})
        else:
            declaracao = DeclaracaoRetroVenda.objects.filter(codigo_imovel=codigo_imovel)
            if declaracao:
                return render(request, 'info.html', {'codigo_imovel': codigo_imovel, 'declaracao': declaracao[0], 'endereco': declaracao[0].endereco})

            return render(request, 'info.html', {'declaracao': None})
    return render(request, 'retrovenda.html')