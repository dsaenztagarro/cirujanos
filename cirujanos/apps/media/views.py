# -*- encoding: utf-8 -*-
from cirujanos.views import AppTemplateView
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str
from django.views.generic import View
import models
import os


class MediaGalleryView(AppTemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        criteria = {'public': True}
        PublicationModel = self.model_klass
        listParamName = "%s_list" % (PublicationModel.__name__.lower(),)

        if PublicationModel.isAchievedByYear():
            date_list = PublicationModel.objects.filter(public=True).dates(
                'publish_date', 'year')
            year_list = [date.year for date in date_list]
            context['year_list'] = reversed(year_list)
            context['publish_year'] = context.get(
                'publish_year', PublicationModel.getLastPublicationYear())
            criteria['publish_date__year'] = context['publish_year']

        modelList = PublicationModel.objects.filter(**criteria)
        context[listParamName] = modelList

        return self.render_to_response(self.decorate_context(context))


class MediaBrowserView(View):
    """
    Opens in the browser the media file
    """
    def get(self, request, *args, **kwargs):
        file_path = self.__get_file_path(kwargs)
        with open(file_path, 'r') as pdf:
            mimetype = self.__get_mimetype(kwargs)
            response = HttpResponse(pdf.read(), mimetype=mimetype)
            response['Content-Disposition'] = 'inline; filename="%s"' % \
                smart_str(os.path.basename(file_path))
            return response
        pdf.closed

    def __get_file_path(self, params):
        document_root = settings.MEDIA_ROOT
        path = os.path.join(document_root, params['path'])
        return smart_str(path)

    def __get_mimetype(self, params):
        path = params['path']
        if 'pdf' in path:
            return 'application/pdf'
        else:
            return None


class MediaDownloadView(View):
    """
    Downloads to the browser client the media file
    """
    def get(self, request, *args, **kwargs):
        document_root = settings.MEDIA_ROOT
        file_path = smart_str(os.path.join(document_root, kwargs['path']))
        response = HttpResponse(mimetype='application/force-download')
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = 'attachment; filename="%s"' % \
            smart_str(os.path.basename(file_path))
        response['X-Sendfile'] = file_path
        return response


class ArticleView(MediaGalleryView):
    """
    Shows a list of all published articles
    """
    template_name = 'media/article/index.html'
    model_klass = models.Article


class MultimediaView(AppTemplateView):
    template_name = 'media/index.html'


class VideoView(MediaGalleryView):
    template_name = 'media/video/index.html'
    model_klass = models.Video


class EventView(MediaGalleryView):
    template_name = 'media/event/index.html'
    model_klass = models.Event


class SlideView(MediaGalleryView):
    template_name = 'media/slide/index.html'
    model_klass = models.Slide


class DisplayVideoView(AppTemplateView):
    template_name = 'media/video/display.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        video = get_object_or_404(models.Video, pk=context['video_id'])
        context['video'] = video

        return self.render_to_response(context)
