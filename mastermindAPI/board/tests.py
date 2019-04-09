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
        self.game.code = ['R', 'G', 'B', 'P']
        self.assertEqual(decode(self.game.code), ['RED', 'GREEN', 'BLUE', 'PURPLE'])

    def test_check_pegs(self):
        self.game.code = ['R', 'G', 'B', 'P']
        combination1 = ['A', 'C', 'Z', 'H']
        combination2 = ['R', 'G', 'Y', 'P']
        combination3 = ['R', 'G', 'B', 'P']
        self.assertEqual(self.game.check_pegs(combination1), (0,0))
        self.assertEqual(self.game.check_pegs(combination2), (0,3))
        self.assertEqual(self.game.check_pegs(combination3), (0,4))