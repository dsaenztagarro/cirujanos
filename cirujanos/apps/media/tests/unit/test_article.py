from django.test import TestCase
from ..support import factories as f


class ArticleTestCase(TestCase):

    def setUp(self):
        self.article = f.ArticleFactory.create()

    def test_display_object_in_django_admin(self):
        self.assertEqual(self.article.__str__(), self.article.title)
