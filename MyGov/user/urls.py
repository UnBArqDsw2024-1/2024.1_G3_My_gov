from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("cadastro/", views.register_user, name="register"),
    path("home/", views.home, name="home"),
    path('logout/', views.logout_user, name='logout'),
]