from cirujanos.tests.support.integration import DownloadTestCase
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from ..support import factories


class ArticleIndexTestCase(DownloadTestCase):

    def setUp(self):
        self.article_list = factories.ArticleFactory.create_batch(3)

        self.driver.get(self.url_for('home:index'))
        # click on "Multimedia" menu
        menu_xpath = ("//ul[@class='nav navbar-nav navbar-right']"
                      "/li/a[text()='%s']"
                      ) % _("media")
        self.driver.find_element_by_xpath(menu_xpath).click()
        # click on "Articles" submenu
        self.driver.find_element_by_css_selector("#articles_title").click()

    def test_show_articles(self):
        for article in self.article_list:
            selector = "#article_%s h6 span" % article.id
            title = self.driver.find_element_by_css_selector(selector).text
            self.assertEqual(title, article.title)

    def test_opens_articles_in_new_window(self):
        for article in self.article_list:
            # Click on "Watch online"
            link_css = "#article_%s a" % article.id
            self.driver.find_element_by_css_selector(link_css).click()

        pdf_windows = self.driver.window_handles
        pdf_windows.pop(0)  # first window is pathology page
        for i, handle in enumerate(pdf_windows):
            self.driver.switch_to.window(handle)
            article = self.article_list[i]
            pdf_url = reverse('media:browser',
                              kwargs={'path': article.file.name})
            self.assertTrue(pdf_url in self.driver.current_url)
