from django.db import models

class Game(models.Model):
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

class Player(models.Model):
    name = models.CharField(max_length=200)
    standort = models.CharField(max_length=200, default="Berlin")
    # name
    # standort
    # auswertung
    # rangliste
