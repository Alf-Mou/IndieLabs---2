from django.urls import path
from game.views import index, indiegame

urlpatterns = [
    path('', index, name='index'),
    path('indiegame/<int:game_id>',indiegame, name='indiegame'),
]