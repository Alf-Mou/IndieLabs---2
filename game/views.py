from django.shortcuts import render, get_object_or_404
from game.models import Games

def index(request):
    game = Games.objects.all()
    return render(request, 'game/index.html', {"game_grupo": game})

def indiegame(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/indiegame.html', {"game": game})