from django.contrib import admin
import models


class PathologyArticleInline(admin.TabularInline):
    model = models.PathologyArticle
    extra = 1


class PathologyVideoInline(admin.TabularInline):
    model = models.PathologyVideo
    extra = 1


class PathologyAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
    list_display_links = ('name',)
    inlines = (PathologyArticleInline, PathologyVideoInline)
    ordering = ('order',)


class ProcedureArticleInline(admin.TabularInline):
    model = models.ProcedureArticle
    extra = 1


class ProcedureVideoInline(admin.TabularInline):
    model = models.ProcedureVideo
    extra = 1


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('order', 'name')
    list_display_links = ('name',)
    inlines = (ProcedureArticleInline, ProcedureVideoInline)
    ordering = ('order',)


admin.site.register(models.Pathology, PathologyAdmin)
admin.site.register(models.Procedure, ProcedureAdmin)
