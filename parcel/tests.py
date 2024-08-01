from django.test import TestCase, Client
from parcel import models as parcel_models
from post_machin import models as post_machin_models
from django.contrib.auth.models import User




# Create your tests here.
class MyTestCase(TestCase):
    fixtures = ['data']

    def setUp(self):
        test_postmachin = post_machin_models.PostMachin.objects.get(pk=1)
        self.test_postmachin = test_postmachin
        test_locker = post_machin_models.Locker.objects.filter(post_machin=test_postmachin).all()[0]
        self.locker_id = test_locker.pk
        self.test_parsel = parcel_models.Parcel()
        self.test_parsel.recipient = User.objects.create_user(username='test_user', password='test_password')
        self.test_parsel.sender = 'John Doe'
        self.test_parsel.size = 3
        self.test_parsel.post_machin = test_postmachin
        self.test_parsel.locker = test_locker
        self.test_parsel.order_date_time = '2021-01-01 10:00:00'
        self.test_parsel.open_date_time = '2021-01-02 10:00:00'
        self.test_parsel.status = False
        self.test_parsel.save()
        self.test_parsel.locker.status = False
        self.test_parsel.locker.save()


    def test_parcel(self):
        actual_locker = post_machin_models.Locker.objects.get(pk=self.test_parsel.locker.pk)
        self.assertEqual(actual_locker.status, False)
        c = Client()
        c.login(username='test_user', password='test_password')

        response = c.post(f'/parcel/{self.test_parsel.pk}/get_parcel/')
        self.assertEqual(response.status_code, 302)
        actual_parcel = parcel_models.Parcel.objects.get(pk=self.test_parsel.pk)
        self.assertEqual(actual_parcel.status, True)
        actual_locker = post_machin_models.Locker.objects.get(pk=self.test_parsel.locker.pk)
        self.assertEqual(actual_locker.status, True)

    def test_parcel_form_get(self):
        c = Client()
        c.login(username='test_user', password='test_password')
        response = c.get('/parcel/parcel_form/')
        self.assertEqual(response.status_code, 200)


    def test_parsel_form_g(self):
        client = Client()
        client.login(username='test_user', password='test_password')
        response  = client.post('/parcel/parcel_form/',{'sender': 'test_user',
                                   'recipient': self.test_parsel.recipient.pk,
                                   'size': 2,
                                   'post_machin': self.test_postmachin.pk})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form.save()')
    def test_parsel_form_g_b(self):
        client = Client()
        client.login(username='test_user', password='test_password')
        response  = client.post('/parcel/parcel_form/',{'sender': 'test_user',
                                   'recipient': "",
                                   'size': 2,
                                   'post_machin': self.test_postmachin.pk})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form.save()',False)
