from django.test import TestCase
from ..support import factories as f


class SlideTestCase(TestCase):

    def setUp(self):
        self.slide = f.SlideFactory.create()

    def test_show_unicode_representation(self):
        self.assertEqual(self.slide.__str__(), self.slide.title)
