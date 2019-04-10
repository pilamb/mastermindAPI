from rest_framework import viewsets

from board.models import Game, Movement
from board.serializers import BoardSerializer, MovementSerializer


class GameView(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = BoardSerializer


class MovementView(viewsets.ReadOnlyModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
