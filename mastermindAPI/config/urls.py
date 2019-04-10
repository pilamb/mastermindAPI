from django.urls import include, path
from rest_framework import routers
from players.views import UserViewSet

from board.views import MovementView


router = routers.DefaultRouter()
router.register(r'players', UserViewSet)
router.register(r'movements', MovementView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
