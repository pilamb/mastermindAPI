from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from board.models import Game, Movement
from board.serializers import BoardSerializer, MovementSerializer


class GameView(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = BoardSerializer

    @action(detail=False, methods=['get'])
    def create_game(self, request):
        context = {
            "request": self.request,
        }
        player = self.request.user
        new_game = Game.objects.create(player=player)
        serializer = BoardSerializer(instance=new_game, context=context)
        return Response(serializer.data)

class MovementView(viewsets.ReadOnlyModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
