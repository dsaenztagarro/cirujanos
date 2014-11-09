from django.test import TestCase
from ..support import factories as f


class VideoTestCase(TestCase):

    def setUp(self):
        self.video = f.VideoFactory.create()

    def test_show_unicode_representation(self):
        self.assertEqual(self.video.__str__(), self.video.title)
