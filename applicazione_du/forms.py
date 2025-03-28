from django import forms
from .models import Giocatore

class GiocatoreForm(forms.ModelForm):
    class Meta:
        model = Giocatore
        fields = ['nome', 'cognome', 'velocita', 'tiro', 'passaggio', 'dribbling', 'difesa', 'fisico', 'ruolo']
        labels = {
            'nome': 'Nome',
            'cognome': 'Cognome',
            'velocita': 'Velocità',  # Corretto con l'accento
            'tiro': 'Tiro',
            'passaggio': 'Passaggio',
            'dribbling': 'Dribbling',
            'difesa': 'Difesa',
            'fisico': 'Fisico',
            'ruolo': 'Ruolo'
        }

        from django import forms
from .models import Giocatore

class OrganizzaPartitaForm(forms.Form):
    NUMERO_GIOCATORI_CHOICES = (
        (10, '5 vs 5'),
        (12, '6 vs 6'),
        (14, '7 vs 7'),
        (16, '8 vs 8'),
        (18, '9 vs 9'),
        (20, '10 vs 10'),
        (22, '11 vs 11'),
        # Aggiungi altri valori se necessario
    )
    
    numero_giocatori = forms.ChoiceField(choices=NUMERO_GIOCATORI_CHOICES)
    giocatori = forms.ModelMultipleChoiceField(queryset=Giocatore.objects.all(), widget=forms.CheckboxSelectMultiple)