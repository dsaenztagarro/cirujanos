from django.db import models
from django.utils.translation import ugettext_lazy as _
import extensions as ext
import datetime


class Article(models.Model, ext.Publication):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to='articles')
    publish_date = models.DateField(default=datetime.date.today)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'media'
        verbose_name = _('article')
        verbose_name_plural = _('articles')


class Video(models.Model, ext.Publication):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    url = models.URLField()
    publish_date = models.DateField(default=datetime.date.today)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'media'
        verbose_name = _('video')
        verbose_name_plural = _('videos')


class Slide(models.Model, ext.Publication):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    file = models.FileField(upload_to='articles')
    publish_date = models.DateField(default=datetime.date.today)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'media'
        verbose_name = _('slide')
        verbose_name_plural = _('slides')


class Event(models.Model, ext.Publication):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    file = models.FileField(upload_to='events')
    publish_date = models.DateField(default=datetime.date.today)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'media'
        verbose_name = _('event')
        verbose_name_plural = _('events')
