from cirujanos.tests.support.integration import DownloadTestCase
# from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from ..support import factories


class PathologyVideosTestCase(DownloadTestCase):

    def setUp(self):
        self.pathology_list = factories.PathologyFactory. \
            create_batch(3, references__videos_count=2)
        self.pathology = self.pathology_list.pop(0)
        self.pathology_videos = self.pathology.videos.all()

        self.driver.get(self.url_for('home:index'))
        # click on "Pathologies" menu
        menu_xpath = ("//ul[@class='nav navbar-nav navbar-right']"
                      "/li/a[@class='dropdown-toggle menu'][text()='%s']"
                      ) % _("pathologies")
        self.driver.find_element_by_xpath(menu_xpath).click()
        # click on "Pathology #1" submenu
        submenu_xpath = "//ul[@class='dropdown-menu']/li/a[text()='%s']" % \
                        self.pathology.name
        self.driver.find_element_by_xpath(submenu_xpath).click()

    def test_show_videos(self):
        for video in self.pathology_videos:
            selector = "#video_%s h6 span" % video.id
            title = self.driver.find_element_by_css_selector(selector).text
            self.assertEqual(title, video.title)

    def test_navigate_to_video(self):
        video = self.pathology_videos.first()
        link_css = "#video_%s a" % video.id
        self.driver.find_element_by_css_selector(link_css).click()
        video_details_title = _("video details").encode('utf-8')
        page_content = self.driver.page_source.encode('utf-8')
        self.assertTrue(video_details_title in page_content)
