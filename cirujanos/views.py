from django.shortcuts import render_to_response
from django.views.generic import DetailView, TemplateView
from mixins import HeaderContextMixin


class AppTemplateView(HeaderContextMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(self.decorate_context(context))


class AppDetailView(HeaderContextMixin, DetailView):
    pass


def error_404_view(request):
    return render_to_response('error404.html')


def error_500_view(request):
    return render_to_response('error500.html')


def tests_view(request):
    return render_to_response('tests.html')
