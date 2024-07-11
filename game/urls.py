from django.urls import path
from game.views import index, indiegame, buscar, todosJogos

urlpatterns = [
    path('', index, name='index'),
    path('indiegame/<int:game_id>',indiegame, name='indiegame'),
    path('buscar', buscar, name='buscar'),
    path('todosJogos', todosJogos, name='todosJogos')
]