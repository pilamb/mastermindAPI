from django.db import models

CODE_CHOICES = (
    ('R', 'RED'),
    ('G', 'GREEN'),
    ('B', 'BLUE'),
    ('O', 'ORANGE'),
    ('P', 'PURPLE'),
    ('Y', 'YELLOW'),
)


class Game(models.Model):
    """
    Represent a board game.
    """

    created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    code = models.CharField(choices=CODE_CHOICES,
                            max_length=4, default=['R', 'G', 'B', 'P'])
