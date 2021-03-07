from django.test import TestCase
from django.contrib.auth.models import User as Player

from rest_framework.exceptions import ValidationError

from board.models import Game, Movement
from board.serializers import BoardSerializer, PlaySerializer, MovementSerializer


class GameSerializersTestCase(TestCase):
    def setUp(self):
        self.player = Player.objects.create()
        self.game = Game.objects.create(player=self.player)
        self.data = {"code": str(self.game.code), "player": self.player}
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
        self.assertEqual(serializer.data.get("code"), str(self.game.code))

    def test_board_has_movements(self):
        self.assertTrue("movements" in self.serializer.fields.keys())


class MovementSerializerTestCase(TestCase):
    def setUp(self):
        self.player = Player.objects.create()
        self.game = Game.objects.create(player=self.player)
        self.movement = Movement.objects.create(
            code=str(self.game.code), game=self.game, player=self.player
        )
        self.data = {
            "game": self.game,
            "player": self.player,
            "code": str(self.game.code),
        }
        self.serializer = MovementSerializer(data=self.data)

    def test_movement_serializer_creation(self):
        self.serializer.is_valid()
        self.assertIsNotNone(self.serializer.data)

    def test_serializer_usage(self):
        serializer = MovementSerializer(instance=self.movement)
        self.assertEqual(serializer.instance, self.movement)

    def test_serializer_is_valid(self):
        serializer = MovementSerializer(data=self.data)
        serializer.is_valid()
        data = serializer.data
        self.assertIsNotNone(data)


class PlaySerializerTestCase(TestCase):
    def test_validate_code_input(self):
        value = list()
        serializer = PlaySerializer(data={"code": value})
        with self.assertRaises(ValidationError):
            serializer.validate_code(value=value)

    def test_validate_code_bad_colors_number(self):
        value = "RED,GREEN"
        serializer = PlaySerializer()
        with self.assertRaises(ValidationError):
            serializer.validate_code(value=str(value))

    def test_validate_bad_colors(self):
        value = "RED,MONKEY,BANANA,SKY"
        serializer = PlaySerializer()
        with self.assertRaises(ValidationError):
            serializer.validate_code(value=str(value))
