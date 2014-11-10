from django.test import TestCase
from cirujanos.apps.web import models
from ..support import factories as f


class ProcedureArticleTestCase(TestCase):

    def setUp(self):
        self.procedure = f.ProcedureFactory.create(
            references__articles_count=1)
        self.article = self.procedure.articles.first()
        self.procedure_article = models.ProcedureArticle.objects.first()

    def test_display_object_in_django_admin(self):
        string_object = "procedure#%s - article#%s" % (self.procedure.id,
                                                       self.article.id)
        self.assertEqual(self.procedure_article.__str__(), string_object)
