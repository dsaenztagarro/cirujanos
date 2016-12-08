from django.conf.urls import url
from cirujanos.apps.home.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="index"),
]
