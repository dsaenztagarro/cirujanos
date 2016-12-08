from django.contrib import admin
from .models import ConfigParam


class ConfigParamAdmin(admin.ModelAdmin):
    model = ConfigParam

admin.site.register(ConfigParam, ConfigParamAdmin)
