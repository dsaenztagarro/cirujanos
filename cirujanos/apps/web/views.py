# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from cirujanos.apps.web.models import (
    Pathology,
    PathologyArticle,
    PathologyVideo,
    Procedure,
    ProcedureArticle,
    ProcedureVideo)
from cirujanos.views import AppDetailView

class PathologyIndexView(View):
    def get(self, request):
        pathology = Pathology.menu_objects.first()
        url = reverse('pathology_detail', kwargs={'slug': pathology.slug})
        return HttpResponseRedirect(url)


class PathologyDetailView(AppDetailView):
    model = Pathology
    template_name = 'web/pathology/index.html'

    def get_context_data(self, **kwargs):
        context = super(PathologyDetailView, self).get_context_data(**kwargs)
        articles = PathologyArticle.objects. \
            filter(pathology=self.object).order_by('order')
        videos = PathologyVideo.objects. \
            filter(pathology=self.object).order_by('order')
        context.update({
            'pathology_detail': self.object,
            'pathology_articles': articles,
            'pathology_videos': videos,
        })
        return self.decorate_context(context)


class ProcedureIndexView(View):
    def get(self, request):
        procedure = Procedure.menu_objects.first()
        url = reverse('procedure_detail', kwargs={'slug': procedure.slug})
        return HttpResponseRedirect(url)


class ProcedureDetailView(AppDetailView):
    model = Procedure
    template_name = 'web/procedure/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProcedureDetailView, self).get_context_data(**kwargs)
        articles = ProcedureArticle.objects. \
            filter(procedure=self.object).order_by('order')
        videos = ProcedureVideo.objects. \
            filter(procedure=self.object).order_by('order')
        context.update({
            'procedure_detail': self.object,
            'procedure_articles': articles,
            'procedure_videos': videos,
        })
        return self.decorate_context(context)
