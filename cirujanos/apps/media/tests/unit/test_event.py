from django.test import TestCase
from ..support import factories as f


class EventTestCase(TestCase):

    def setUp(self):
        self.event = f.EventFactory.create()

    def test_display_object_in_django_admin(self):
        self.assertEqual(self.event.__str__(), self.event.title)
