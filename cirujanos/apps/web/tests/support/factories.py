import factory
from ....web.models import Pathology, PathologyArticle, PathologyVideo
from cirujanos.apps.media.tests.support import factories


class PathologyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Pathology

    name = factory.Sequence(lambda n: 'Pathology #{0}'.format(n))
    order = factory.Sequence(lambda n: n)
    content = factory.Sequence(
        lambda n: "<p><strong>Content for Pathology #%s</strong></p>" % n)

    @factory.post_generation
    def references(self, create, extracted, **kwargs):
        if not create:
            return

        if 'articles_count' in kwargs:
            count = kwargs['articles_count']
            article_list = factories.ArticleFactory.create_batch(count)
            for i, article in enumerate(article_list):
                PathologyArticle.objects.create_and_save(self, article, i)

        if 'videos_count' in kwargs:
            count = kwargs['videos_count']
            video_list = factories.VideoFactory.create_batch(count)
            for i, video in enumerate(video_list):
                PathologyVideo.objects.create_and_save(self, video, i)
