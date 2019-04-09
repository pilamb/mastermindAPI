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

def decode(code):
    """
    Like get_code_display's Django but for a tuple.
    Display human readable color names instead of only a letter.
    """
    return [name for i in code for item, name in CODE_CHOICES if item == i]


class Game(models.Model):
    """
    Represent a board game.
    Responsible for turn count, generating
    the colors code, and the game main management
    """

    created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    code = models.CharField(choices=CODE_CHOICES,
                            max_length=4, default=create_code)
    player = models.ForeignKey('auth.User',
                               related_name="games",
                               on_delete=models.CASCADE)
    class Meta:
        ordering = ('created',)

    @property
    def get_code_display(self):
        return decode(self.code)

    def check_combination(self, combination):
        return combination == self.code

    def check_pegs(self, combination):
        """
        Count for right colors in wrong place,
        and for right colors in the right place
        """
        white_pegs = 0  # but not a match in the right place
        black_pegs = 0  # right color and in right place
        for position, item in enumerate(combination):
            if item.upper() in self.code and item == self.code[position]:
                black_pegs += 1
            elif item.upper() in self.code:
                white_pegs += + 1
        return white_pegs, black_pegs

    def end_game(self):
        self.finished = True
    
    def check_combination(self, combination):
        return combination == self.code
