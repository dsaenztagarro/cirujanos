from django.test import TestCase
from ..support import factories as f


class EventTestCase(TestCase):

    def setUp(self):
        self.event = f.EventFactory.create()

    def test_show_unicode_representation(self):
        self.assertEqual(self.event.__str__(), self.event.title)
