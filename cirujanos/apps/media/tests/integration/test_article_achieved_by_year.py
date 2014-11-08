from cirujanos.models import ConfigParam
from cirujanos.apps.media.extensions import Publication
from cirujanos.tests.support.integration import IntegrationTestCase
from django.utils.translation import ugettext as _
from ..support import factories as f
from datetime import datetime, timedelta


class ArticleAchievedByYearTestCase(IntegrationTestCase):

    def setUp(self):
        ConfigParam(param_name='ARTICLE_ACHIEVED_BY_YEAR',
                    param_value=Publication.TRUE,
                    description='Articles achieved by year').save()

        today = datetime.now()
        year = timedelta(days=365)

        for i in xrange(3):
            date = today - i * year
            articles = f.ArticleFactory.create_batch(3, publish_date=date)
            setattr(self, 'year%s' % i, date.year)
            setattr(self, 'year%s_articles' % i, articles)

        self.driver.get(self.url_for('home:index'))
        # click on "Multimedia" menu
        menu_xpath = ("//ul[@class='nav navbar-nav navbar-right']"
                      "/li/a[text()='%s']"
                      ) % _("media")
        self.driver.find_element_by_xpath(menu_xpath).click()
        # click on "Articles" submenu
        self.driver.find_element_by_css_selector("#articles_title").click()

    def teardown(self):
        ConfigParam.objects.all().delete()

    def test_show_year_links(self):
        for i in xrange(3):
            year = getattr(self, 'year%s' % i)
            year_selector = '#year_%s' % year
            link_el = self.driver.find_element_by_css_selector(year_selector)
            self.assertEqual(link_el.text, str(year))

    def test_show_articles_for_each_year(self):
        for i in xrange(3):
            year = getattr(self, 'year%s' % i)
            articles = getattr(self, 'year%s_articles' % i)
            self.driver.find_element_by_css_selector('#year_%s' % year).click()

            for article in articles:
                selector = "#article_%s h6 span" % article.id
                title = self.driver.find_element_by_css_selector(selector).text
                self.assertEqual(title, article.title)
