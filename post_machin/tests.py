from django.test import TestCase, Client
from django.urls import reverse

from parcel import models as parcel_models
from post_machin import models as post_machin_models
from django.contrib.auth.models import User

from post_machin.models import PostMachin, Locker


class MyTestCase(TestCase):
    fixtures = ['data']

    def setUp(self):
        self.test_postmachin = post_machin_models.PostMachin.objects.get(pk=1)
        self.test_locker = post_machin_models.Locker.objects.filter(post_machin=self.test_postmachin).all()[0]


    def test_post_machin_view(self):
        c = Client()
        c.login(username='test_user', password='test_password')
        response = c.get('/post_machines/')
        self.assertEqual(response.status_code, 200)

    def test_one_post_machin_view(self):
        response = self.client.get(f'/post_machines/{self.test_postmachin.pk}/')
        self.assertEqual(response.status_code, 200)


