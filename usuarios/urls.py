from django.urls import path
from usuarios.views import cadastro, login

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
]