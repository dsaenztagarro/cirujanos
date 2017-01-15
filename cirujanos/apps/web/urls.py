from django.conf.urls import url
from cirujanos.apps.web.views import (
    PathologyDetailView,
    PathologyIndexView,
    ProcedureDetailView,
    ProcedureIndexView,
)

urlpatterns = [
    url(r'^pathology/$', PathologyIndexView.as_view(), name="pathology"),
    url(r'^pathology/(?P<slug>[-\w]+)/$', PathologyDetailView.as_view(),
        name='pathology_detail'),

    url(r'^procedure/$', ProcedureIndexView.as_view(), name="procedure"),
    url(r'^procedure/(?P<slug>[-\w]+)/$', ProcedureDetailView.as_view(),
        name='procedure_detail')
]
