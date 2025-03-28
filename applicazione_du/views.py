from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Giocatore
from .forms import GiocatoreForm
from random import shuffle
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def crea_giocatore(request):
    if request.method == 'POST':
        form = GiocatoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizza_giocatori')  
    else:
        form = GiocatoreForm()
    return render(request, 'crea_giocatore.html', {'form': form})

def formatta_overall(giocatori):
    for giocatore in giocatori:
        giocatore.overall = int(giocatore.overall)
    return giocatori

def visualizza_giocatori(request):
    giocatori = Giocatore.objects.all().order_by('cognome')
    giocatori = formatta_overall(giocatori)
    return render(request, 'visualizza_giocatori.html', {'giocatori': giocatori})

def calcola_overall_medio(squadra):
    if not squadra:
        return 0
    overall_giocatori = [giocatore.overall for giocatore in squadra]
    print(f"Overall di tutti i giocatori nella squadra: {overall_giocatori}")
    somma_overall = sum(overall_giocatori)
    print(f"Somma degli overall: {somma_overall}")
    overall_medio = round(somma_overall / len(squadra), 2)
    print(f"Overall medio calcolato per squadra: {overall_medio}")
    return overall_medio



# Aggiungi questa importazione all'inizio del tuo file views.py
from operator import attrgetter

def menu_principale(request):
    return render(request, 'menu_principale.html')

def organizza_partita(request):
    if request.method == 'POST':
        giocatori_selezionati_ids = request.POST.getlist('giocatori_selezionati')
        giocatori_selezionati = Giocatore.objects.filter(id__in=giocatori_selezionati_ids).order_by('cognome')
        
        # Calcola l'overall di ciascun giocatore e mescola l'elenco dei giocatori
        giocatori_selezionati = list(giocatori_selezionati)
        shuffle(giocatori_selezionati)
        
        # Dividi i giocatori in due squadre
        meta = len(giocatori_selezionati) // 2
        squadra_1 = giocatori_selezionati[:meta]
        squadra_2 = giocatori_selezionati[meta:]
        
        overall_medio_squadra_1 = calcola_overall_medio(squadra_1)
        overall_medio_squadra_2 = calcola_overall_medio(squadra_2)

        print(f"Overall medio Squadra 1: {overall_medio_squadra_1}")
        print(f"Overall medio Squadra 2: {overall_medio_squadra_2}")
        
        return render(request, 'squadre.html', {
            'squadra_1': squadra_1, 
            'squadra_2': squadra_2, 
            'overall_medio_squadra_1': overall_medio_squadra_1,
            'overall_medio_squadra_2': overall_medio_squadra_2
        })
    else:
        giocatori = Giocatore.objects.all().order_by('cognome')  # Ordina i giocatori per cognome
        return render(request, 'organizza_partita.html', {'giocatori': giocatori})


def rigenera_squadre(request):
    if request.method == 'POST':
        squadra_1_ids = request.POST.getlist('squadra_1')
        squadra_2_ids = request.POST.getlist('squadra_2')

        # Recupera gli oggetti Giocatore dai loro ID
        squadra_1 = list(Giocatore.objects.filter(id__in=squadra_1_ids))
        squadra_2 = list(Giocatore.objects.filter(id__in=squadra_2_ids))
        
        # Combina e mischia i giocatori
        giocatori_totali = squadra_1 + squadra_2
        shuffle(giocatori_totali)
        
        # Ridistribuisci i giocatori tra le due squadre
        meta = len(giocatori_totali) // 2
        nuova_squadra_1 = giocatori_totali[:meta]
        nuova_squadra_2 = giocatori_totali[meta:]
        
        overall_medio_nuova_squadra_1 = calcola_overall_medio(nuova_squadra_1)
        overall_medio_nuova_squadra_2 = calcola_overall_medio(nuova_squadra_2)

        print(f"Overall medio Nuova Squadra 1: {overall_medio_nuova_squadra_1}")
        print(f"Overall medio Nuova Squadra 2: {overall_medio_nuova_squadra_2}")
        
        return render(request, 'squadre.html', {
            'squadra_1': nuova_squadra_1, 
            'squadra_2': nuova_squadra_2,
            'overall_medio_squadra_1': overall_medio_nuova_squadra_1,
            'overall_medio_squadra_2': overall_medio_nuova_squadra_2
        })
    else:
        return redirect('organizza_partita')


    
def modifica_giocatore(request, giocatore_id):
    giocatore = get_object_or_404(Giocatore, id=giocatore_id)
    if request.method == 'POST':
        form = GiocatoreForm(request.POST, instance=giocatore)
        if form.is_valid():
            form.save()
            return redirect('visualizza_giocatori')
    else:
        form = GiocatoreForm(instance=giocatore)
    return render(request, 'crea_giocatore.html', {'form': form, 'giocatore': giocatore})

def elimina_giocatore(request, giocatore_id):
    giocatore = get_object_or_404(Giocatore, id=giocatore_id)
    giocatore.delete()
    return redirect('visualizza_giocatori')

def seleziona_giocatore(request):
    if request.method == 'POST':
        giocatore_id = request.POST.get('giocatore_id')
        # Aggiungi qui la logica per elaborare il giocatore selezionato
        # Ad esempio, puoi salvare l'ID del giocatore selezionato nel database
        return JsonResponse({'messaggio': 'Giocatore selezionato con successo'})
    return JsonResponse({'errore': 'Richiesta non valida'}, status=400)

def cerca_giocatori(request):
    query = request.GET.get('q', '')
    if query:
        giocatori = Giocatore.objects.filter(nome__icontains=query)
        results = []
        for giocatore in giocatori:
            results.append({
                'id': giocatore.id,
                'name': giocatore.nome,
                'overall': giocatore.overall,
            })
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})