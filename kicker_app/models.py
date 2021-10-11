from django.db import models

class Spiel(models.Model):
    datetime = models.CharField(max_length=200)
    standort = models.CharField(max_length=200)
    modus = models.CharField(max_length=200)
    teammitglieder = models.CharField(max_length=200)
    # datum, uhrzeit
    # standort
    # modus
    # teammitglieder
    # position spieler
    # ergebnis

class Spieler(models.Model):
    name = models.CharField(max_length=200)
    # name
    # standort
    # auswertung
    # rangliste
