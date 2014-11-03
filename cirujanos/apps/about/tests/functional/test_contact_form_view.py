from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from ..support.factories import NotificationEmailFactory


class ContactFormViewTestCase(TestCase):

    def setUp(self):
        receiver_list = NotificationEmailFactory.create_batch(2)
        self.to = [receiver.email for receiver in receiver_list]
        context = {
            'name': 'test user',
            'phone': '999-999-999',
            'message': 'Message sent by test user',
            'email': 'test.user@gmail.com'
        }
        self.resp = self.client.post(reverse('about:contact-us'), context)
        self.client = Client()

    def test_send_email(self):
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject,
                         settings.CONTACT_EMAIL_SUBJECT)
        self.assertEqual(mail.outbox[0].to, self.to)

    def test_show_success_message(self):
        self.assertEqual(self.resp.status_code, 302)
