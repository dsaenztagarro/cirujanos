from django.test import TestCase
from ..support import factories as f


class NotificationEmailTestCase(TestCase):

    def setUp(self):
        self.notification_email = f.NotificationEmailFactory.create()

    def test_display_object_in_django_admin(self):
        self.assertEqual(self.notification_email.__str__(),
                         self.notification_email.email)
