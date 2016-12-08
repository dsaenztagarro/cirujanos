from django.conf.urls import url
from cirujanos.apps.media.views import (
    ArticleView,
    DisplayVideoView,
    EventView,
    MediaBrowserView,
    MultimediaView,
    SlideView,
    VideoView)


urlpatterns = [
    url(r'^$', MultimediaView.as_view(), name="index"),
    url(r'^articles/$', ArticleView.as_view(), name="articles"),
    url(r'^videos/$', VideoView.as_view(), name="videos"),
    url(r'^events/$', EventView.as_view(), name="events"),
    url(r'^slides/$', SlideView.as_view(), name="slides"),
    url(r'^videos/(?P<video_id>\d)/$', DisplayVideoView.as_view(),
        name="video-display"),
    url(r'^browser/(?P<path>.*)$', MediaBrowserView.as_view(), name='browser'),
    # url(r'^download/(?P<path>.*)$', MediaDownloadView.as_view(),
    #     name='download'),
]

urlpatterns += [
    url(r'^articles/(?P<publish_year>\d{4})/$',
        ArticleView.as_view(), name="articles_year"),
]

urlpatterns += [
    url(r'^videos/(?P<publish_year>\d{4})/$',
        VideoView.as_view(), name="videos_year"),
]
