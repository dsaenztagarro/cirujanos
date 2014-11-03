# -*- encoding: utf-8 -*-
from cirujanos.mixins import BackboneFormAdapterMixin, HeaderContextMixin
from cirujanos.views import AppTemplateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView
from forms import ContactForm
from models import Doctor
import json


class AboutView(AppTemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({"doctor_list": Doctor.objects.all()})
        return self.decorate_context(context)


class ContactFormView(HeaderContextMixin, BackboneFormAdapterMixin, FormView):
    """
    A view for displaying contact form and rendering a template response on
    html submissions or sending a json response on json form submission.
    """
    template_name = 'about/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.send_email()
        response = super(ContactFormView, self).form_valid(form)
        if self.request.is_ajax():
            context = {
                'title': _("message success"),
                'message': _("contact notification success")
            }
            return HttpResponse(json.dumps(context),
                                content_type='application/json')
        else:
            return response


class DoctorContentView(AppTemplateView):
    """
    A view for displaying information about a doctor
    """
    template_name = 'about/doctor.html'

    def get_context_data(self, **kwargs):
        context = super(DoctorContentView, self).get_context_data(**kwargs)
        doctor = get_object_or_404(Doctor, code=context['doctor_code'])
        doctorcontent_list = doctor.doctorcontent_set.order_by('content_type')
        context = {
            "doctor": doctor,
            "doctorcontent_list": doctorcontent_list
        }
        return context
