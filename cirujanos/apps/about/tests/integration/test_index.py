from django.utils.translation import ugettext as _
from cirujanos.tests.support import test_base


class AboutIndexTest(test_base.IntegrationTestCase):

    def test_send_contact_email(self):
        self.driver.get(self.url_for('about:index'))
        # element = self.driver.find_element_by_id('articles_title')
        # element.click()
        # body = self.driver.find_element_by_tag_name('body')
        # article_title = _("media article title")
        # self.assertIn(article_title, body.text)
