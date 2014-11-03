from django import template
from django.utils.translation import ugettext as _

register = template.Library()


@register.inclusion_tag('media/extras/media_type_record.html')
def media_type_record(media_type):
    url_path = "media:%ss" % (media_type,)
    image_path = 'img/media/%s_128x128.png' % (media_type,)
    media = {'url_path': url_path,
             'image_path': image_path,
             'title': _(media_type + "s"),
             'description': _(media_type + "s watch collection")}
    return {
        'media': media,
        'media_type': "%ss" % media_type
    }


@register.inclusion_tag('media/extras/article_record.html')
def article_record(article, **kwargs):
    context = {'article': article}
    context.update(kwargs)
    return context


@register.inclusion_tag('media/extras/video_record.html')
def video_record(video, **kwargs):
    context = {'video': video}
    context.update(kwargs)
    return context


@register.inclusion_tag('media/extras/slide_record.html')
def slide_record(slide, **kwargs):
    context = {'slide': slide}
    context.update(kwargs)
    return context


@register.inclusion_tag('media/extras/event_record.html')
def event_record(event, **kwargs):
    context = {'event': event}
    context.update(kwargs)
    return context
