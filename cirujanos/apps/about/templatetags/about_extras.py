# -*- coding: utf-8 -*-
from django import template
from django.utils.translation import ugettext as _

register = template.Library()


@register.inclusion_tag('about/extras/doctor.html')
def show_doctor(doctor):
    context = {
        'doctor': doctor
    }
    return context


@register.inclusion_tag('about/extras/doctor_content.html')
def show_doctorcontent(doctor_content):
    context = {
        'title': title(doctor_content),
        'doctorcontent': doctor_content
    }
    return context


def title(doctor_content):
    content_type_code = doctor_content.content_type.code
    try:
        return _("about doctorcontenttype %s" % content_type_code)
    except:
        return content_type_code
