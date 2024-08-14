from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("cadastro/", views.register_user, name="register"),
]