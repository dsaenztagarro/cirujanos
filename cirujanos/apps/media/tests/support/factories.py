from django.utils import timezone
from cirujanos.apps.web import models
import factory
import os


TEST_MEDIA_PATH = os.path.join(os.path.dirname(__file__), '..', 'fixtures',
                               'media')
TEST_ARTICLE_PATH = os.path.join(TEST_MEDIA_PATH, 'article_dummy.pdf')


class ArticleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Article

    title = factory.Sequence(lambda n: 'Article #{0}'.format(n))
    author = factory.Sequence(lambda n: 'Author #{0}'.format(n))
    description = factory.Sequence(lambda n: 'Description #%s' % n)
    file = factory.django.FileField(from_path=TEST_ARTICLE_PATH)
    publish_date = timezone.now()
    public = True


class VideoFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Video

    title = factory.Sequence(lambda n: 'Video #{0}'.format(n))
    author = factory.Sequence(lambda n: 'Author #{0}'.format(n))
    description = factory.Sequence(lambda n: 'Description #%s' % n)
    url = 'http://www.youtube.com/embed/e0QF2Ld1skM'
    publish_date = timezone.now()
    public = True
