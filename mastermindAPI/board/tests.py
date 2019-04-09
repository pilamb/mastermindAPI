from django.test import TestCase

from board.models import Game


class BoardTestCase(TestCase):

    def setUp(self):
        self.game = Game.objects.create()

    def test_create_game(self):
        self.assertIsNotNone(self.game)

    def test_code_game(self):
        self.assertEqual(self.game.code, ['R', 'G', 'B', 'P'])
