from django.test import TestCase
from ..support import factories as f


class SliderTestCase(TestCase):

    def setUp(self):
        self.slider = f.SliderFactory.create()

    def test_show_unicode_representation(self):
        self.assertEqual(self.slider.__str__(), self.slider.name)
