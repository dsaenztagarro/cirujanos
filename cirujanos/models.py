from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxLengthValidator
from django.db import models


class ConfigParam(models.Model):
    param_name = models.CharField(max_length=100)
    param_value = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.param_name
