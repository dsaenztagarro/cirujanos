from django.test import TestCase
from cirujanos.models import ConfigParam


class ConfigParamTestCase(TestCase):

    def setUp(self):
        self.param_name = 'ARTICLE_ACHIEVED_BY_YEAR'
        self.config_param = ConfigParam(param_name=self.param_name,
                                        param_value='T',
                                        description='Test param')
        self.config_param.save()

    def test_show_unicode_representation(self):
        self.assertEqual(self.config_param.__str__(), self.param_name)