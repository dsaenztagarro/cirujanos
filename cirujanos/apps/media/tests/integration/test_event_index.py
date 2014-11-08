from cirujanos.tests.support.integration import DownloadTestCase
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from ..support import factories


class EventIndexTestCase(DownloadTestCase):

    def setUp(self):
        self.event_list = factories.EventFactory.create_batch(3)

        self.driver.get(self.url_for('home:index'))
        # click on "Multimedia" menu
        menu_xpath = ("//ul[@class='nav navbar-nav navbar-right']"
                      "/li/a[text()='%s']"
                      ) % _("media")
        self.driver.find_element_by_xpath(menu_xpath).click()
        # click on "Events" submenu
        self.driver.find_element_by_css_selector("#events_title").click()

    def test_show_events(self):
        for event in self.event_list:
            selector = "#event_%s h6 span" % event.id
            title = self.driver.find_element_by_css_selector(selector).text
            self.assertEqual(title, event.title)

    def test_opens_events_in_new_window(self):
        for event in self.event_list:
            # Click on "Watch online"
            link_css = "#event_%s a" % event.id
            self.driver.find_element_by_css_selector(link_css).click()

        pdf_windows = self.driver.window_handles
        pdf_windows.pop(0)  # first window is pathology page
        for i, handle in enumerate(pdf_windows):
            self.driver.switch_to.window(handle)
            event = self.event_list[i]
            pdf_url = reverse('media:browser',
                              kwargs={'path': event.file.name})
            self.assertTrue(pdf_url in self.driver.current_url)
