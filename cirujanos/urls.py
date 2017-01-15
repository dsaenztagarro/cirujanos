from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from . import views
admin.autodiscover()

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='coming-soon.html')),
    url(r'^$', lambda r: HttpResponseRedirect('home/')),
    url(r'^home/', include('cirujanos.apps.home.urls', namespace="home")),
    url(r'^web/', include('cirujanos.apps.web.urls')),
    url(r'^multimedia/', include('cirujanos.apps.media.urls',
                                 namespace="media")),
    url(r'^about/', include('cirujanos.apps.about.urls', namespace="about")),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^tests/$', views.tests_view),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# from django.conf import settings
# if settings.DEBUG:
#    urlpatterns += patterns(
#        '',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#            {'document_root': '/path'}),
#    )

handler404 = 'cirujanos.views.error_404_view'
handler500 = 'cirujanos.views.error_500_view'
