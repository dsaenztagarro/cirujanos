from django.contrib import admin
from cirujanos.apps.home.models import Slider, Post


class SliderAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
    list_display_links = ('name',)
    ordering = ('order',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title',)
    # ordering = ('order',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Post, PostAdmin)
