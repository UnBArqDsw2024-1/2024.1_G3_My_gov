from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Model User extendendo AbstractUser
class User(AbstractUser):
  password = models.CharField(max_length=128, default='')
  date_of_birth = models.DateField(null=True, blank=True)
  tipo_pessoa = models.CharField(max_length=50, default='')
  rg = models.CharField(max_length=20, default='')
  orgao_emissor = models.CharField(max_length=50, default='')
  uf_emissor = models.CharField(max_length=2, default='')
  estrangeiro = models.BooleanField(default=False)
  estado_civil = models.CharField(max_length=50, default='')
  ddd = models.IntegerField(null=True, blank=True)
  celular = models.IntegerField(null=True, blank=True)

  # Adicionando related_name para evitar conflitos
  groups = models.ManyToManyField(
      'auth.Group',
      related_name='custom_user_set',  # Nome personalizado para evitar conflito
      blank=True,
      help_text='The groups this user belongs to.',
      verbose_name='groups',
  )
  user_permissions = models.ManyToManyField(
      'auth.Permission',
      related_name='custom_user_permissions_set',  # Nome personalizado para evitar conflito
      blank=True,
      help_text='Specific permissions for this user.',
      verbose_name='user permissions',
  )