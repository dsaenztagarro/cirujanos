from cirujanos.apps.web.models import Pathology, Procedure
import json


class HeaderContextMixin(object):
    """
    A mixin that adds to context view the header menus info for every page
    """

    def decorate_context(self, context):
        context['pathology_list'] = Pathology.menu_objects.all()
        context['procedure_list'] = Procedure.menu_objects.all()
        return context


class BackboneFormAdapterMixin(object):
    """
    A mixin that provides support for Backbone Ajax POST requests to
    django.views.generic.edit.FormView

    The issue is that by default Backbone sends the POST data as a JSON encoded
    string in the body of the request not as a part of the request.POST
    QueryDict. So to get the data in this case you would have to use the python
    json library and call json.loads(request.body) in the Django view to read
    the data properly.
    """

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.get_request_data(),
                'files': self.request.FILES,
            })
        return kwargs

    def get_request_data(self):
        if self.request.is_ajax():
            return json.loads(self.request.body)
        else:
            return self.request.POST
