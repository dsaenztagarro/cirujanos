from django.contrib import admin
from .models import (
    Pathology,
    PathologyVideo,
    Procedure,
    ProcedureArticle,
    ProcedureVideo,
    PathologyArticle)


class PathologyArticleInline(admin.TabularInline):
    model = PathologyArticle
    extra = 1


class PathologyVideoInline(admin.TabularInline):
    model = PathologyVideo
    extra = 1


class PathologyAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
    list_display_links = ('name',)
    inlines = (PathologyArticleInline, PathologyVideoInline)
    ordering = ('order',)


class ProcedureArticleInline(admin.TabularInline):
    model = ProcedureArticle
    extra = 1


class ProcedureVideoInline(admin.TabularInline):
    model = ProcedureVideo
    extra = 1


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
    list_display_links = ('name',)
    inlines = (ProcedureArticleInline, ProcedureVideoInline)
    ordering = ('order',)


admin.site.register(Pathology, PathologyAdmin)
admin.site.register(Procedure, ProcedureAdmin)
