from django.shortcuts import render, get_object_or_404, redirect
from game.models import Game
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    game = Game.objects.all()
    return render(request, 'game/index.html', {"game_grupo": game})

def indiegame(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/indiegame.html', {"game": game})

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