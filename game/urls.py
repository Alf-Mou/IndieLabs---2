from django.urls import path
from game.views import index, indiegame, cadastro, login

urlpatterns = [
    path('', index, name='index'),
    path('indiegame/<int:game_id>',indiegame, name='indiegame'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login')
]