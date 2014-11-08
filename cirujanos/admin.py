from django.contrib import admin
import models


class ConfigParamAdmin(admin.ModelAdmin):
    model = models.ConfigParam

admin.site.register(models.ConfigParam, ConfigParamAdmin)
