from django.test import TestCase
from cirujanos.apps.web import models
from ..support import factories as f


class PathologyArticleTestCase(TestCase):

    def setUp(self):
        self.pathology = f.PathologyFactory.create(
            references__articles_count=1)
        self.article = self.pathology.articles.first()
        self.pathology_article = models.PathologyArticle.objects.first()

    def test_display_object_in_django_admin(self):
        string_object = "pathology#%s - article#%s" % (self.pathology.id,
                                                       self.article.id)
        self.assertEqual(self.pathology_article.__str__(), string_object)
