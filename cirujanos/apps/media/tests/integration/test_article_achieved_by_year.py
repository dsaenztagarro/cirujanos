from cirujanos.models import ConfigParam
from cirujanos.apps.media.extensions import Publication
from cirujanos.tests.support.integration import IntegrationTestCase
from django.utils.translation import ugettext as _
from ..support import factories
import time


class ArticleAchievedByYearTestCase(IntegrationTestCase):

    def setUp(self):
        ConfigParam(param_name='ARTICLE_ACHIEVED_BY_YEAR',
                    param_value=Publication.TRUE,
                    description='Articles achieved by year').save()

        self.article_list = factories.ArticleFactory.create_batch(3)

        self.driver.get(self.url_for('home:index'))
        # click on "Multimedia" menu
        menu_xpath = ("//ul[@class='nav navbar-nav navbar-right']"
                      "/li/a[text()='%s']"
                      ) % _("media")
        self.driver.find_element_by_xpath(menu_xpath).click()
        # click on "Articles" submenu
        self.driver.find_element_by_css_selector("#articles_title").click()
        import pdb
        pdb.set_trace()

    def test_show_articles_for_each_year(self):
        import pdb
        pdb.set_trace()
        for article in self.article_list:
            selector = "#article_%s h6 span" % article.id
            title = self.driver.find_element_by_css_selector(selector).text
            self.assertEqual(title, article.title)
