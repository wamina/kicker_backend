from kicker_app.models import Game, Player
from rest_framework_json_api import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('standort', 'datetime', 'player1', 'posP1', 'player2', 'posP2', 'player3', 'posP3', 'player4', 'posP4', 'winner1', 'winner2')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'standort')