from rest_framework import serializers

from .models import Game, Movement


class BoardSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='get_code_display')
    player = serializers.ReadOnlyField(source='player.username')
    finished = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = ('player', 'created', 'code', 'finished')
