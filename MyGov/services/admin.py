from django.contrib import admin
from .models import Endereco, Information, DeclaracaoRetroVenda

# Register your models here.

admin.site.register(Endereco)
admin.site.register(Information)
admin.site.register(DeclaracaoRetroVenda)