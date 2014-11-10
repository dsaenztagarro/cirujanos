from django.test import TestCase
from ..support import factories as f


class SliderTestCase(TestCase):

    def setUp(self):
        self.slider = f.SliderFactory.create()

    def test_display_object_in_django_admin(self):
        self.assertEqual(self.slider.__str__(), self.slider.name)
