from django.contrib import admin
from cirujanos_web.system.models import ConfigParam


class ConfigParamAdmin(admin.ModelAdmin):
    list_display = ('param_name', 'param_value')
    list_display_links = ('param_name',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ConfigParam, ConfigParamAdmin)
