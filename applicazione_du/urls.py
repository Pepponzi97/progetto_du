from django.urls import path
from . import views
from .views import visualizza_giocatori, crea_giocatore, modifica_giocatore, elimina_giocatore, organizza_partita, rigenera_squadre, cerca_giocatori

urlpatterns = [
    path('', views.menu_principale, name='menu_principale'),
    path('', views.visualizza_giocatori, name='home'),  # Aggiungi questa riga per mappare l'URL radice
    path('visualizza_giocatori/', views.visualizza_giocatori, name='visualizza_giocatori'),
    path('crea_giocatore/', views.crea_giocatore, name='crea_giocatore'),
    path('modifica_giocatore/<int:giocatore_id>/', views.modifica_giocatore, name='modifica_giocatore'),
    path('elimina_giocatore/<int:giocatore_id>/', views.elimina_giocatore, name='elimina_giocatore'),
    path('organizza_partita/', views.organizza_partita, name='organizza_partita'),
    path('rigenera_squadre/', views.rigenera_squadre, name='rigenera_squadre'),  # Aggiunta del percorso per rigenerare le squadre
    path('cerca_giocatori/', views.cerca_giocatori, name='cerca_giocatori'),
    # Altre definizioni di percorsi URL...
]