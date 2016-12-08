from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
from .managers import MenuManager, PathologyArticleManager, \
    PathologyVideoManager, ProcedureArticleManager, ProcedureVideoManager
from cirujanos.apps.media.models import Article, Video


class Pathology(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name='URL Slug')
    order = models.IntegerField(default=0)
    content = HTMLField()

    articles = models.ManyToManyField(Article, through='PathologyArticle')
    videos = models.ManyToManyField(Video, through='PathologyVideo')

    objects = models.Manager()  # The default manager.
    menu_objects = MenuManager()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pathology, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pathology_detail', kwargs={'slug': self.slug})

    class Meta:
        app_label = 'web'
        verbose_name = _('pathology')
        verbose_name_plural = _('pathologies')


class PathologyArticle(models.Model):
    pathology = models.ForeignKey(Pathology)
    article = models.ForeignKey(Article)
    order = models.IntegerField(default=0)

    objects = PathologyArticleManager()

    def __unicode__(self):
        return "pathology#%s - article#%s" % \
            (self.pathology.id, self.article.id)

    class Meta:
        app_label = 'web'


class PathologyVideo(models.Model):
    pathology = models.ForeignKey(Pathology)
    video = models.ForeignKey(Video)
    order = models.CharField(default='A', max_length=3)

    objects = PathologyVideoManager()

    def __unicode__(self):
        return "pathology#%s - video#%s" % \
            (self.pathology.id, self.video.id)

    class Meta:
        app_label = 'web'


class Procedure(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name='URL Slug')
    order = models.IntegerField(default=0)
    content = HTMLField()

    articles = models.ManyToManyField(Article, through='ProcedureArticle')
    videos = models.ManyToManyField(Video, through='ProcedureVideo')

    objects = models.Manager()  # The default manager.
    menu_objects = MenuManager()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Procedure, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('procedure_detail', kwargs={'slug': self.slug})

    class Meta:
        app_label = 'web'
        verbose_name = _('procedure')
        verbose_name_plural = _('procedures')


class ProcedureArticle(models.Model):
    procedure = models.ForeignKey(Procedure)
    article = models.ForeignKey(Article)
    order = models.IntegerField(default=0)

    objects = ProcedureArticleManager()

    def __unicode__(self):
        return "procedure#%s - article#%s" % \
            (self.procedure.id, self.article.id)

    class Meta:
        app_label = 'web'


class ProcedureVideo(models.Model):
    procedure = models.ForeignKey(Procedure)
    video = models.ForeignKey(Video)
    order = models.CharField(default='A', max_length=3)

    objects = ProcedureVideoManager()

    def __unicode__(self):
        return "procedure#%s - video#%s" % \
            (self.procedure.id, self.video.id)

    class Meta:
        app_label = 'web'
