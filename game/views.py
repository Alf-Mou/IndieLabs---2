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
    game = Game.objects.all()
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            game = game.filter(nome__icontains=nome_a_buscar)

    return render(request, 'game/buscar.html', {"game_grupo": game})

def todosJogos(request):
    game = Game.objects.all()
    return render(request, 'game/todosJogos.html', {"game_grupo": game})