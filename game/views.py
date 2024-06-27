from django.shortcuts import render, get_object_or_404
from game.models import Game

def index(request):
    game = Game.objects.all()
    return render(request, 'game/index.html', {"game_grupo": game})

def indiegame(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/indiegame.html', {"game": game})

def cadastro(request):
    return render(request, 'game/cadastro.html')

def login(request):
    return render(request, 'game/login.html')

def buscar(request):
    return render(request, 'game/buscar.html')

def todosJogos(request):
    game = Game.objects.all()
    return render(request, 'game/todosJogos.html', {"game_grupo": game})