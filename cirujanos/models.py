from django.db import models


class ConfigParam(models.Model):
    param_name = models.CharField(max_length=100)
    param_value = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.param_name
