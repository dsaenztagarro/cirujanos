from django.conf.urls import patterns, url
from views import AboutView, ContactFormView, DoctorContentView


urlpatterns = patterns(
    '',
    url(r'^$', AboutView.as_view(), name="index"),
    # url(r'^contact/$', 'cirujanos.apps.about.views.contact_us', name="contact"),
    url(r'^doctor/(?P<doctor_code>\w+)/$', DoctorContentView.as_view(),
        name="doctor"),
    url(r'^contact/$', ContactFormView.as_view(), name="contact-us"),
)
