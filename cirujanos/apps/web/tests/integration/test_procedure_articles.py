from cirujanos.tests.support.integration import DownloadTestCase
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from ..support import factories


class ProcedureArticlesTestCase(DownloadTestCase):

    def setUp(self):
        self.procedure_list = factories.ProcedureFactory. \
            create_batch(3, references__articles_count=2)
        self.procedure = self.procedure_list.pop(0)
        self.procedure_articles = self.procedure.articles.all()

        self.driver.get(self.url_for('home:index'))
        # click on "Pathologies" menu
        menu_xpath = ("//ul[@class='nav navbar-nav navbar-right']"
                      "/li/a[@class='dropdown-toggle menu'][text()='%s']"
                      ) % _("procedures")
        self.driver.find_element_by_xpath(menu_xpath).click()
        # click on "Procedure #1" submenu
        submenu_xpath = "//ul[@class='dropdown-menu']/li/a[text()='%s']" % \
                        self.procedure.name
        self.driver.find_element_by_xpath(submenu_xpath).click()

    def test_show_articles(self):
        for article in self.procedure_articles:
            selector = "#article_%s h6 span" % article.id
            title = self.driver.find_element_by_css_selector(selector).text
            self.assertEqual(title, article.title)

    def test_opens_articles_in_new_window(self):
        for article in self.procedure_articles:
            # Click on "Watch online"
            link_css = "#article_%s a" % article.id
            self.driver.find_element_by_css_selector(link_css).click()

        pdf_windows = self.driver.window_handles
        pdf_windows.pop(0)  # first window is procedure page
        for i, handle in enumerate(pdf_windows):
            self.driver.switch_to.window(handle)
            article = self.procedure_articles[i]
            pdf_url = reverse('media:browser',
                              kwargs={'path': article.file.name})
            self.assertTrue(pdf_url in self.driver.current_url)
