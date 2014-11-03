from django.db import models


class MenuManager(models.Manager):
    def get_queryset(self):
        return super(MenuManager, self).get_queryset().order_by('order')


class PathologyArticleManager(models.Manager):
    def create_and_save(self, pathology, article, order):
        pathology_article = self.create(pathology=pathology, article=article,
                                        order=order)
        return pathology_article.save()


class PathologyVideoManager(models.Manager):
    def create_and_save(self, pathology, video, order):
        pathology_video = self.create(pathology=pathology, video=video,
                                      order=order)
        return pathology_video.save()


class ProcedureArticleManager(models.Manager):
    def create_and_save(self, procedure, article, order):
        procedure_article = self.create(procedure=procedure, article=article,
                                        order=order)
        return procedure_article.save()


class ProcedureVideoManager(models.Manager):
    def create_and_save(self, procedure, video, order):
        procedure_video = self.create(procedure=procedure, video=video,
                                      order=order)
        return procedure_video.save()
