from cirujanos.tests.support.integration import DownloadTestCase
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from ..support import factories


class SlideIndexTestCase(DownloadTestCase):

    def setUp(self):
        self.slide_list = factories.SlideFactory.create_batch(3)

        self.driver.get(self.url_for('home:index'))
        # click on "Multimedia" menu
        menu_xpath = ("//ul[@class='nav navbar-nav navbar-right']"
                      "/li/a[text()='%s']"
                      ) % _("media")
        self.driver.find_element_by_xpath(menu_xpath).click()
        # click on "Slides" submenu
        self.driver.find_element_by_css_selector("#slides_title").click()

    def test_show_slides(self):
        for slide in self.slide_list:
            selector = "#slide_%s h6 span" % slide.id
            title = self.driver.find_element_by_css_selector(selector).text
            self.assertEqual(title, slide.title)

    def test_opens_slides_in_new_window(self):
        for slide in self.slide_list:
            # Click on "Watch online"
            link_css = "#slide_%s a" % slide.id
            self.driver.find_element_by_css_selector(link_css).click()

        pdf_windows = self.driver.window_handles
        pdf_windows.pop(0)  # first window is pathology page
        for i, handle in enumerate(pdf_windows):
            self.driver.switch_to.window(handle)
            slide = self.slide_list[i]
            pdf_url = reverse('media:browser',
                              kwargs={'path': slide.file.name})
            self.assertTrue(pdf_url in self.driver.current_url)
