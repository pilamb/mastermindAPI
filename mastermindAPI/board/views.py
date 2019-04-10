from rest_framework import viewsets

from board.models import Movement
from board.serializers import MovementSerializer


class MovementView(viewsets.ReadOnlyModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
