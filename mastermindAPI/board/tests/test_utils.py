from unittest import TestCase

from django.conf import settings

from board.utils import check_quantity, transform_to_letters, validate_input


class UtilsTestCase(TestCase):
    def setUp(self):
        self.bad_code_1 = [1, 2, 3, 'A']
        self.bad_code_2 = ['MAGENTA', 'PINK', 'BLACK', 'WHITE']
        self.bad_length_code = ['BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE']
        self.ok_code = ['RED', 'GREEN', 'BLUE', 'RED']

    def test_validate_input(self):
        self.assertEqual(validate_input(self.ok_code), True)
        self.assertEqual(validate_input(self.bad_code_2), False)
        self.assertEqual(validate_input(self.bad_code_1), False)

    def test_check_input_length(self):
        self.assertEqual(check_quantity(self.bad_length_code), False)
        self.assertTrue(check_quantity(self.ok_code), settings.MAX_PEGS)

    def test_color_translation(self):
        self.assertEqual(transform_to_letters(self.ok_code),
                         ['R', 'G', 'B', 'R'])
