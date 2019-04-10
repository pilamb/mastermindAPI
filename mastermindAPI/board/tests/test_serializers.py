import mock

from django.test import TestCase
from rest_framework.serializers import ValidationError

from board.models import Game, Movement
from board.serializers import Game


class GameSerializersTestCase(TestCase):

    def test_game_serializer(self):
        pass