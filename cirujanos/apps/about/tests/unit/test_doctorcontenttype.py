from django.test import TestCase
from ..support import factories as f


class DoctorContentTypeTestCase(TestCase):

    def setUp(self):
        self.doctor_content_type = f.DoctorContentTypeFactory.create()

    def test_display_object_in_django_admin(self):
        self.assertEqual(self.doctor_content_type.__str__(),
                         self.doctor_content_type.code)
