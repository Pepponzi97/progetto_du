from django.db import models

class Giocatore(models.Model):
    RUOLI_CHOICES = (
        ('P', 'Portiere'),
        ('D', 'Difensore'),
        ('C', 'Centrocampista'),
        ('A', 'Attaccante'),
    )

    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    velocita = models.IntegerField(default=1)
    tiro = models.IntegerField(default=1)
    passaggio = models.IntegerField(default=1)
    dribbling = models.IntegerField(default=1)
    difesa = models.IntegerField(default=1)
    fisico = models.IntegerField(default=1)
    ruolo = models.CharField(max_length=1, choices=RUOLI_CHOICES)
    overall = models.IntegerField(default=1)  # Cambiato da DecimalField a IntegerField

    def save(self, *args, **kwargs):
        # Calcola l'Overall basato sulle caratteristiche del giocatore
        caratteristiche = [self.velocita, self.tiro, self.passaggio, self.dribbling, self.difesa, self.fisico]
        totale = sum(caratteristiche)
        self.overall = round(totale / len(caratteristiche)) if len(caratteristiche) > 0 else 0
        super(Giocatore, self).save(*args, **kwargs)
