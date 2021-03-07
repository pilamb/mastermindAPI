from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from board.models import Game, Movement
from board.serializers import BoardSerializer, PlaySerializer, MovementSerializer


class GameView(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = BoardSerializer

    @action(
        detail=False,
        methods=["GET"],
        url_name="create",
        permission_classes=(permissions.IsAuthenticated,),
    )
    def create_game(self, request):
        context = {
            "request": self.request,
        }
        player = self.request.user
        new_game = Game.objects.create(player=player)
        serializer = BoardSerializer(instance=new_game, context=context)
        creation_message = "Creating board (this turn doesnt count as a movement.)"
        Movement.objects.create(game=new_game, player=player, result=creation_message)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["POST"],
        url_name="code_guess",
        permission_classes=(permissions.IsAuthenticated,),
    )
    def play(self, request, pk=None):
        try:
            game = Game.objects.get(id=pk)
        except Game.DoesNotExist:
            return Response({"Game not found!"}, status=status.HTTP_404_NOT_FOUND)
        if game.finished:
            return Response(
                {"status": "This game has already finished."},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )
        context = {
            "request": self.request,
        }
        serializer = PlaySerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.validated_data.update({"game": Game.objects.get(id=pk)})
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)


class MovementView(viewsets.ReadOnlyModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
