from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
import os
import datetime


class Slider(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    enable = models.BooleanField(default=False)
    content = models.TextField()

    def __unicode__(self):
        return self.name

    @classmethod
    def active(cls):
        return cls.objects.filter(enable=True).order_by("order")

    class Meta:
        verbose_name = _('slider')
        verbose_name_plural = _('sliders')


class Post(models.Model):
    order = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    publish_date = models.DateField(default=datetime.date.today)
    is_system = models.BooleanField(default=False)
    system_image_path = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/home/posts/',
        default=os.path.join(settings.STATIC_ROOT, 'images', 'home', 'posts',
                             'default.jpg'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=200)
