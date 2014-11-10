from django.test import TestCase
from cirujanos.apps.web import models
from ..support import factories as f


class ProcedureVideoTestCase(TestCase):

    def setUp(self):
        self.procedure = f.ProcedureFactory.create(
            references__videos_count=1)
        self.video = self.procedure.videos.first()
        self.procedure_video = models.ProcedureVideo.objects.first()

    def test_display_object_in_django_admin(self):
        string_object = "procedure#%s - video#%s" % (self.procedure.id,
                                                     self.video.id)
        self.assertEqual(self.procedure_video.__str__(), string_object)
