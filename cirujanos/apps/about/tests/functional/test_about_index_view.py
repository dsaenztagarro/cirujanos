from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from ..support import factories


class AboutViewTestCase(TestCase):
    SIZE = 3  # number of doctors

    def setUp(self):
        self.doctor_list = [factories.DoctorFactory.create()
                            for i in range(0, self.SIZE)]
        self.client = Client()

    def test_show_doctors(self):
        resp = self.client.get(reverse('about:index'))
        self.assertTrue('doctor_list' in resp.context)
        self.assertEqual(resp.context['doctor_list'].count(), self.SIZE)
        doctor_list = resp.context['doctor_list']
        for index, doctor in enumerate(doctor_list):
            self.assertEqual(doctor, self.doctor_list[index])
