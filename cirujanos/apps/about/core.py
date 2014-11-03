from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from models import NotificationEmail


class ContactEmailDispatcher(object):
    def __init__(self, form_data):
        self.form_data = form_data
        self.context = Context(form_data)
        self.template = {
            'plain': get_template('about/templates/contact_form.txt'),
            'html': get_template('about/templates/contact_form.html')
        }

    def run(self):
        subject = settings.CONTACT_EMAIL_SUBJECT
        from_email = settings.DEFAULT_FROM_EMAIL
        msg = EmailMultiAlternatives(subject, self.plain_text_content(),
                                     from_email, self.contact_receiver_list())
        msg.attach_alternative(self.html_content(), "text/html")
        msg.send()

    def plain_text_content(self):
        return self.template['plain'].render(self.context)

    def html_content(self):
        return self.template['html'].render(self.context)

    def contact_receiver_list(self):
        receiver_list = NotificationEmail.objects.all()
        return [receiver.email for receiver in receiver_list]
