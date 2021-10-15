from django.db import models
from datetime import datetime

class Game(models.Model):
    standort = models.CharField(max_length=200, default="Berlin")
    datetime = models.CharField(max_length=200, default="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
    player1 = models.CharField(max_length=200, default="Max Mustermann")
    posP1 = models.CharField(max_length=200, default="vorne/hinten")
    player2 = models.CharField(max_length=200, default="Max Mustermann")
    posP2 = models.CharField(max_length=200, default="vorne/hinten")
    player3 = models.CharField(max_length=200, default="Max Mustermann")
    posP3 = models.CharField(max_length=200, default="vorne/hinten")
    player4 = models.CharField(max_length=200, default="Max Mustermann")
    posP4 = models.CharField(max_length=200, default="vorne/hinten")
    winner1 = models.CharField(max_length=200, default="Max Mustermann")
    winner2 = models.CharField(max_length=200, default="Max Mustermann")
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
