from django.db import models


class Game(models.Model):
    """
    Represent a board game.
    """

    created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
