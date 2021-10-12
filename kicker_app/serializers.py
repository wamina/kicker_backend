from kicker_app.models import Game, Player
from rest_framework_json_api import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('datetime', 'standort', 'modus', 'teammitglieder')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'standort')