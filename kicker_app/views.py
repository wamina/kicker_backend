from rest_framework.views import APIView
from rest_framework.response import Response
from kicker_app.models import Game, Player
from kicker_app.serializers import GameSerializer, PlayerSerializer
from rest_framework import viewsets, status

from rest_framework.decorators import api_view


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer