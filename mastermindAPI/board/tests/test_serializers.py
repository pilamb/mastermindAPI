from django.test import TestCase
from django.contrib.auth.models import User as Player

from rest_framework.serializers import ValidationError

from board.models import Game, Movement
from board.serializers import BoardSerializer


class GameSerializersTestCase(TestCase):

    def test_board_serializer(self):
        player = Player.objects.create()
        game = Game.objects.create(player=player)
        serializer = BoardSerializer(data={'code': str(game.code),
                                           'player':player})
        self.assertIsNotNone(serializer.instance)