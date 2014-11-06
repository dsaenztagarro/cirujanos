from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
import os


class IntegrationTestCase(LiveServerTestCase):

    @classmethod
    def browser_profile(cls):
        return webdriver.FirefoxProfile()

    @classmethod
    def setUpClass(cls):
        cls.caps = webdriver.DesiredCapabilities.FIREFOX
        cls.caps['tunnel-identifier'] = os.environ['TRAVIS_JOB_NUMBER']
        cls.caps['build'] = os.environ['TRAVIS_BUILD_NUMBER']
        cls.caps['tags'] = [os.environ['TRAVIS_PYTHON_VERSION'], 'CI']

        cls.driver = webdriver.Remote(
            command_executor=settings.SELENIUM_COMMAND_EXECUTOR,
            desired_capabilities=cls.caps,
            browser_profile=cls.browser_profile(),
        )
        cls.driver.implicitly_wait(20)
        super(IntegrationTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(IntegrationTestCase, cls).tearDownClass()

    def url_for(self, path):
        return '%s%s' % (self.live_server_url, reverse(path))


class DownloadTestCase(IntegrationTestCase):

    @classmethod
    def browser_profile(cls):
        profile = webdriver.FirefoxProfile()

        # "browser.download.folderList": controls the default folder to
        # download a file to. 0 indicates the Desktop; 1 indicates the systems
        # default downloads location; 2 indicates a custom folder
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting",
                               False)
        profile.set_preference('browser.download.manager.focusWhenStarting',
                               False)
        profile.set_preference('browser.download.useDownloadDir', True)
        profile.set_preference('browser.helperApps.alwaysAsk.force', False)
        profile.set_preference('browser.download.manager.alertOnEXEOpen',
                               False)
        profile.set_preference('browser.download.manager.closeWhenDone', True)
        profile.set_preference('browser.download.manager.showAlertOnComplete',
                               False)
        profile.set_preference('browser.download.manager.useWindow', False)
        profile.set_preference("browser.download.dir", os.getcwd())
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "application/pdf")

        # disable Firefox's built-in PDF viewer
        profile.set_preference("pdfjs.disabled", True)

        # disable Adobe Acrobat PDF preview plugin
        profile.set_preference("plugin.scan.plid.all", False)
        profile.set_preference("plugin.scan.Acrobat", "99.0")

        profile.update_preferences()

        return profile
