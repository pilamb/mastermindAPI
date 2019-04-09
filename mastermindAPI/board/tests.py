import mock

from django.test import TestCase

from board.models import Game, create_code, decode


class BoardTestCase(TestCase):

    def setUp(self):
        self.game = Game.objects.create()

    def test_create_game(self):
        self.assertIsNotNone(self.game)

    def test_create_code(self):
        with mock.patch("random.choices",
                        return_value=['R', 'G', 'B', 'P']):
            self.assertEqual(create_code(), ['R', 'G', 'B', 'P'])

    def test_delete(self):
        self.game.delete()
        self.assertEqual(Game.objects.count(), 0)

    def test_check_combination(self):
        combination = ['R', 'G', 'B', 'P']
        game = Game.objects.create()
        game.code = ['R', 'G', 'B', 'P']
        self.assertEqual(game.check_combination(combination=combination), True)

    def test_get_code_display(self):
        game = Game.objects.create()
        game.code = ['R', 'G', 'B', 'P']
        self.assertEqual(decode(game.code), ['RED', 'GREEN', 'BLUE', 'PURPLE'])
