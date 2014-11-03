from django import template
# from django.utils.translation import ugettext as _

register = template.Library()


@register.inclusion_tag('web/extras/references.html', takes_context=True)
def references(context, web_content):
    articles = context[web_content + '_articles']
    videos = context[web_content + '_videos']
    return {
        'articles': articles if (len(articles) > 0) else None,
        'videos': videos if (len(videos) > 0) else None
    }
