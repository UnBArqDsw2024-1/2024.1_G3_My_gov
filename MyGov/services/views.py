from django.shortcuts import render

def index(request):
    context = {
        'message': "Hello, world. You're at the services index."
    }
    return render(request, 'index.html', context)