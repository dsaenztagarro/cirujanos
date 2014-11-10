from cirujanos.tests.support.integration import SeleniumTestCase
from django.utils.translation import ugettext as _


class MediaIndexTest(SeleniumTestCase):

    def test_visit_articles(self):
        self.driver.get(self.url_for('media:index'))
        element = self.driver.find_element_by_id('articles_title')
        element.click()
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn(_("articles"), body.text)
