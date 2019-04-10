from django.test import TestCase
from django.contrib.auth.models import User as Player

from board.models import Game, Movement
from board.serializers import BoardSerializer, MovementSerializer


class GameSerializersTestCase(TestCase):
    def setUp(self):
        self.player = Player.objects.create()
        self.game = Game.objects.create(player=self.player)
        self.data = {'code': str(self.game.code), 'player': self.player}
        self.serializer = BoardSerializer(data=self.data)

    def test_board_serializer(self):
        serializer = BoardSerializer(instance=self.game)
        self.assertIsNotNone(serializer.instance)

    def test_board_serializer_is_valid(self):
        self.assertTrue(self.serializer.is_valid())

    def test_board_serializer_creation(self):
        serializer = BoardSerializer(data=self.data)
        serializer.is_valid()
        self.assertIsNotNone(serializer.data)
        self.assertEqual(serializer.data.get('code'), str(self.game.code))

class MovementSerializer(TestCase):
    def test_movement_serializer(self):
        pass