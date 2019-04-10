from rest_framework import serializers

from .models import Game, Movement



class MovementSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='get_code_display')
    player = serializers.ReadOnlyField(source='player.username')
    created = serializers.DateTimeField()
    game = serializers.HyperlinkedRelatedField(many=False,
                                               read_only=True,
                                               view_name='game-detail')
    result = serializers.CharField()
    class Meta:
        model = Movement
        fields = ('code', 'player', 'created', 'game', 'result')


class BoardSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='get_code_display')
    player = serializers.ReadOnlyField(source='player.username')
    finished = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = ('player', 'created', 'code', 'finished')

