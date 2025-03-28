from django.contrib import admin
from .models import Giocatore

@admin.register(Giocatore)
class GiocatoreAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'velocita', 'tiro', 'passaggio', 'dribbling', 'difesa', 'fisico', 'ruolo', 'overall')
