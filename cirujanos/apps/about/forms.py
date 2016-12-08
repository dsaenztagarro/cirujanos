# -*- encoding: utf-8 -*-
from django import forms
from cirujanos.apps.about.core import ContactEmailDispatcher


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        dispatcher = ContactEmailDispatcher(self.cleaned_data)
        dispatcher.run()
