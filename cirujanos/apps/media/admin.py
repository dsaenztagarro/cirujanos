from django.contrib import admin
from models import Article, Video, Slide, Event


class AdminArticle(admin.ModelAdmin):
    pass


class AdminVideo(admin.ModelAdmin):
    pass


class AdminEvent(admin.ModelAdmin):
    pass


class AdminSlide(admin.ModelAdmin):
    pass


admin.site.register(Article, AdminArticle)
admin.site.register(Video, AdminVideo)
admin.site.register(Event, AdminEvent)
admin.site.register(Slide, AdminSlide)
