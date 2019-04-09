import random

from django.db import models


CODE_CHOICES = (
    ('R', 'RED'),
    ('G', 'GREEN'),
    ('B', 'BLUE'),
    ('O', 'ORANGE'),
    ('P', 'PURPLE'),
    ('Y', 'YELLOW'),
)


def create_code():
    """
    Generate the secret combination.
    """
    return random.choices([i for i, j in CODE_CHOICES], k=4)


class Game(models.Model):
    """
    Represent a board game.
    """

    created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    code = models.CharField(choices=CODE_CHOICES,
                            max_length=4, default=create_code)

    def check_combination(self, combination):
        return combination == self.code
