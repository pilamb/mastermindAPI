import mock

from django.test import TestCase

from board.models import Game, create_code


class BoardTestCase(TestCase):

    def setUp(self):
        self.game = Game.objects.create()

    def test_create_game(self):
        self.assertIsNotNone(self.game)

    def test_create_code(self):
        with mock.patch("random.choices",
                        return_value=['R', 'G', 'B', 'P']):
            self.assertEqual(create_code(), ['R', 'G', 'B', 'P'])
