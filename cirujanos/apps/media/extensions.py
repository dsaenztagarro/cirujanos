from django.db import models
from cirujanos.models import ConfigParam


class Publication():

    TRUE = "T"
    FALSE = "F"

    @classmethod
    def getMostCurrentYear(cls):
        """ Returns the most current year of publication of an article.
        Only articles with status "public" are considered. """
        dictionary_date = cls.objects.filter(public=True).aggregate(
            models.Max('publish_date'))
        if dictionary_date['publish_date__max'] is not None:
            return dictionary_date['publish_date__max'].year
        return 0

    @classmethod
    def isAchievedByYear(cls):
        """ Returns True if all multimedia items are shown indexed by year.
        On the other hand returns False if all multimedia items are shown
        together """
        key = "%s_ACHIEVED_BY_YEAR" % (cls.__name__.upper())
        try:
            configParam = ConfigParam.objects.get(param_name=key)
            return configParam.param_value == cls.TRUE
        except ConfigParam.DoesNotExist:
            pass
        return False
