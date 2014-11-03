from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from ..support import factories


class AboutDoctorTestCase(TestCase):
    SIZE = 3  # number of contents for each doctor

    def setUp(self):
        self.doctor = factories.DoctorFactory.create()
        self.doctorcontent_list = factories.DoctorContentFactory.create_batch(
            self.SIZE,
            doctor=self.doctor
        )
        self.client = Client()

    def test_show_doctorcontent(self):
        kwargs = {'doctor_code': self.doctor.code}
        resp = self.client.get(reverse('about:doctor', kwargs=kwargs))
        self.assertEqual(self.doctor, resp.context['doctor'])
        self.assertEqual(self.SIZE, len(resp.context['doctorcontent_list']))
