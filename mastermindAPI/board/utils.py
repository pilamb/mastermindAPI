from django.conf import settings

from board.models import CODE_CHOICES


COLORS_LIST = [i for _, i in CODE_CHOICES]


def validate_input(input_data):
    """
    Check if user color input exists
    """
    for element in input_data:
        if not isinstance(element, str) or element.strip(" ") not in COLORS_LIST:
            return False
    return True


def check_quantity(input_data):
    """Check if the number of colors is correct"""
    return len(input_data) == settings.MAX_PEGS


def clean_input(input_data):
    """splits string user input into a list comma separated"""
    return input_data.split(",")


def transform_to_letters(input_data):
    """
    :param input_data: ['RED', 'GREEN', 'BLUE', 'GREEN']
    :return ['R', 'G', 'B', 'G']
    """
    letters = list()
    for i in input_data:
        for _, color_name in CODE_CHOICES:
            if i.strip(" ") == color_name:
                letters.append(_)

    return letters
