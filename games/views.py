from django.shortcuts import render
from games.models import Games

def index(request):
    return render(request, 'games/index.html')