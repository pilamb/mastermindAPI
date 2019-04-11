from django.contrib.auth.models import User as Player
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, \
    force_authenticate

from board.models import Game
from board.views import GameView


class BoardViewsTestCase(APITestCase):
    def setUp(self):
        self.user = Player.objects.create()
        self.factory = APIRequestFactory()

    def test_game_list(self):
        url = reverse('game-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_game_create(self):
        url = reverse('game-create')
        view = GameView.as_view({'get':'create_game'})
        request = self.factory.get(url)
        force_authenticate(request, self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('created', response.data)
        self.assertTrue(len(response.data) > 2)
        self.assertTrue(Game.objects.count()==1)

    def test_game_detail(self):
        url = reverse('game-create')
        view = GameView.as_view({'get': 'create_game'})
        request = self.factory.get(url)
        force_authenticate(request, self.user)
        response = view(request)
        # check after detail after creation
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = 'game-detail/{}'.format(Game.objects.first().pk)
        request = self.factory.get(url)
        force_authenticate(request, self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_game_unauthenticated(self):
        url = reverse('game-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
