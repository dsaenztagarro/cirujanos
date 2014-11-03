from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.utils.translation import ugettext as _
from ..support.factories import NotificationEmailFactory
import json


class ContactFormViewWithAjaxTestCase(TestCase):
    NOTIFICATION_EMAIL_COUNT = 3

    def setUp(self):
        receiver_list = NotificationEmailFactory.create_batch(
            self.NOTIFICATION_EMAIL_COUNT)
        self.to = [receiver.email for receiver in receiver_list]

        data = {
            'name': 'test user',
            'phone': '999-999-999',
            'message': 'Message sent by test user',
            'email': 'test.user@gmail.com'
        }
        json_string = json.dumps(data)
        self.client = Client()
        self.resp = self.client.post(reverse('about:contact-us'),
                                     content_type='application/json',
                                     data=json_string,
                                     HTTP_X_REQUESTED_WITH='XMLHttpRequest')

    def test_return_success_status_code(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_send_email(self):
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject,
                         settings.CONTACT_EMAIL_SUBJECT)
        self.assertEqual(mail.outbox[0].to, self.to)

    def test_return_success_message(self):
        title = _("message success")
        message = _("contact notification success")

        json_string = self.resp.content
        data = json.loads(json_string)

        self.assertEqual(data["title"], title)
        self.assertEqual(data["message"], message)
