from django.contrib import admin
from game.models import Game

class ListandoGame(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 10

admin.site.register(Game, ListandoGame)
