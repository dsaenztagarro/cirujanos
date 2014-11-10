from django.test import TestCase
from cirujanos.apps.web import models
from ..support import factories as f


class PathologyVideoTestCase(TestCase):

    def setUp(self):
        self.pathology = f.PathologyFactory.create(
            references__videos_count=1)
        self.video = self.pathology.videos.first()
        self.pathology_video = models.PathologyVideo.objects.first()

    def test_display_object_in_django_admin(self):
        string_object = "pathology#%s - video#%s" % (self.pathology.id,
                                                     self.video.id)
        self.assertEqual(self.pathology_video.__str__(), string_object)
