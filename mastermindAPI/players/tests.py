from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework import status

from players.serializers import UserSerializer
from players.views import UserViewSet


class GeneralUserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test1')
        User.objects.create(username='test2')

    def test_user_serializer(self):
        client = Client()
        response = client.get('/players/')
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        self.assertEqual(len(serializer.instance), 2)
        # auth enabled
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_view(self):
        view = UserViewSet
        query1 = view.queryset.first()
        query2 = User.objects.filter(is_staff=False,
                                     is_active=True).order_by(
                                     '-date_joined').first()
        self.assertAlmostEqual(query1, query2)
