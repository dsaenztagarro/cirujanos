# -*- encoding: utf-8 -*-
from cirujanos.views import AppTemplateView
from .models import Slider, Post


class HomeView(AppTemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            "active_menu": "home",
            "body_class": "pull_top",
            "slider_list": Slider.active(),
            "post_list": Post.objects.all()
        })
        return context
