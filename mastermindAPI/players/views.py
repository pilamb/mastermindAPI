from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.filter(is_staff=False, is_active=True).order_by(
        "-date_joined"
    )
    serializer_class = UserSerializer
