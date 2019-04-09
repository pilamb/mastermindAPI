from django.test import TestCase

from board.models import Game


class BoardTestCase(TestCase):

    def test_create_game(self):
        game = Game.objects.create()
        self.assertIsNotNone(game)
