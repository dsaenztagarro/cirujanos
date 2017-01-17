from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

class Location(models.Model):
    name      = models.CharField(max_length = 50,  default = None)
    address   = models.CharField(max_length = 250, default = None)
    latitude  = models.CharField(max_length = 20,  default = None)
    longitude = models.CharField(max_length = 20,  default = None)

    class Meta:
        app_label = 'about'
        verbose_name = _('about.location')
        verbose_name_plural = _('about.locations')


class DoctorDecorator():
    def image_path(self):
        return 'img/about/doctor/' + self.code + '.png'

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Doctor(DoctorDecorator, models.Model):
    code       = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 50)
    last_name  = models.CharField(max_length = 100)
    job        = models.CharField(max_length = 300)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        app_label = 'about'
        verbose_name = _('doctor')
        verbose_name_plural = _('doctors')


class DoctorContentDecorator():
    def image_path(self):
        return 'img/about/doctor_content_type/%s.png' % (
            self.content_type.code)

    def section_id(self):
        return '#%s' % self.content_type.code

    def has_content_details(self):
        return (self.content_details is not None and
                self.content_details.strip() != "")


class DoctorContent(DoctorContentDecorator, models.Model):
    doctor = models.ForeignKey('Doctor')
    content_type = models.ForeignKey('DoctorContentType')
    content_preview = HTMLField()
    content_details = HTMLField(blank=True, null=True)

    def __unicode__(self):
        return unicode("%s : %s" % (
            self.doctor.first_name, self.content_type.code))

    class Meta:
        app_label = 'about'
        verbose_name = _('doctorcontent')
        verbose_name_plural = _('doctorcontents')


class DoctorContentType(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.code

    class Meta:
        app_label = 'about'
        verbose_name = _('doctorcontenttype')
        verbose_name_plural = _('doctorcontenttypes')


class NotificationEmail(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email

    class Meta:
        app_label = 'about'
        verbose_name = _('contact notification receiver')
        verbose_name_plural = _('contact notification receivers')
