from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from board.views import GameView, index, MovementView
from players.views import UserViewSet



router = routers.DefaultRouter()
router.register(r'players', UserViewSet)
router.register(r'games', GameView)
router.register(r'movements', MovementView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

