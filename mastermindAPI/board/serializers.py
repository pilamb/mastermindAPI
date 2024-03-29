from django.conf import settings
from django.db import transaction

from rest_framework import serializers
from django.db import transaction

from .models import Game, Movement
from .utils import check_quantity, clean_input, transform_to_letters, validate_input

MAX_TURNS = settings.MAX_TURNS
MAX_PEGS = settings.MAX_PEGS


class PlaySerializer(serializers.ModelSerializer):
    code = serializers.CharField(help_text="enter comma separated colors.")
    player = serializers.HiddenField(default=serializers.CurrentUserDefault())
    result = serializers.ReadOnlyField()

    def validate_code(self, value):
        if not isinstance(value, str):  # detected in test
            raise serializers.ValidationError("Error in data input.")
        value = clean_input(value)
        if not validate_input(value):
            raise serializers.ValidationError("Wrong color, please try again.")
        if not check_quantity(value):
            raise serializers.ValidationError("The number of colors is wrong.")
        return transform_to_letters(value)

    def create(self, validated_data):
        game_over = False
        current_game = validated_data.get("game")
        game = Game.objects.select_for_update().get(id=current_game.id)
        code = validated_data.get("code")
        white_pegs, black_pegs = game.check_pegs(code)
        turns_count = game.movements.count()
        feedback = dict()
        if black_pegs == MAX_PEGS:
            result = {"message": "Congratulations, you have won."}
            game_over = True
        elif turns_count == MAX_TURNS:
            # creating a game from the API counts like a movement
            result = {"message": "This was your last turn: Game Over."}
            game_over = True
        else:
            result = {"white_pegs": white_pegs, "black_pegs": black_pegs}
        if game_over:
            with transaction.atomic():
                # Avoiding possible malicious operations
                game.end_game()
        feedback.update(result)
        movement = Movement.objects.create(**validated_data, result=feedback)
        return movement

    class Meta:
        model = Movement
        fields = ("code", "player", "result")


class MovementSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source="get_code_display")
    player = serializers.ReadOnlyField(source="player.username")
    created = serializers.DateTimeField()
    game = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="game-detail"
    )

    result = serializers.CharField()

    class Meta:
        model = Movement
        fields = ("code", "player", "created", "game", "result")


class BoardSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source="get_code_display")
    player = serializers.ReadOnlyField(source="player.username")
    finished = serializers.ReadOnlyField()
    movements = MovementSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ("player", "created", "code", "finished", "movements")
