import mock

from django.test import TestCase
from django.contrib.auth.models import User

from board.models import Game, create_code, decode, Movement


class BoardTestCase(TestCase):

    def setUp(self):
        self.player = User.objects.create(username="test")
        self.game = Game.objects.create(player=self.player)

    def test_create_game(self):
        self.assertIsNotNone(self.game)
        self.assertIsNotNone(self.game.code)
        self.assertIs(self.game.finished, False)

    def test_create_code(self):
        with mock.patch("random.choices",
                        return_value=['R', 'G', 'B', 'P']):
            self.assertEqual(create_code(), ['R', 'G', 'B', 'P'])

    def test_delete(self):
        self.game.delete()
        self.assertEqual(Game.objects.count(), 0)

    def test_check_combination(self):
        combination = ['R', 'G', 'B', 'P']
        combination2 = ['R', 'G', 'B', 'Z']
        game = Game(code = ['R', 'G', 'B', 'P'])
        self.assertEqual(game.check_combination(combination=combination), True)
        self.assertFalse(game.check_combination(combination2))

    def test_get_code_display(self):
        self.game.code = ['R', 'G', 'B', 'P']
        self.assertEqual(decode(self.game.code), ['RED', 'GREEN', 'BLUE', 'PURPLE'])

    def test_check_pegs(self):
        self.game.code = ['R', 'G', 'B', 'P']
        combination1 = ['A', 'C', 'Z', 'H']
        combination2 = ['R', 'G', 'Y', 'P']
        combination3 = ['R', 'G', 'B', 'P']
        combination4 = ['A', 'Z', 'C', 'R']
        self.assertEqual(self.game.check_pegs(combination1), (0,0))
        self.assertEqual(self.game.check_pegs(combination2), (0,3))
        self.assertEqual(self.game.check_pegs(combination3), (0,4))
        self.assertEqual(self.game.check_pegs(combination4), (1,0))

    def test_finish_game(self):
        self.game.end_game()
        self.assertIs(self.game.finished, True)

    def test_game_player(self):
        self.assertIsNotNone(self.game.player)

    def test_game_owner(self):
        self.assertEqual(self.game.player.username, self.player.username)


class MovementTestCase(TestCase):

    def test_create_movement(self):
        m = Movement.objects.create()
        self.assertIsNotNone(m)