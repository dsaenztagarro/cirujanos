from cirujanos.tests.support.integration import SeleniumTestCase
from django.core.urlresolvers import reverse
from cirujanos.apps.web.tests.support import factories as f
from cirujanos.apps.home.tests.support.factories import PostFactory


class PathologyIndexTestCase(SeleniumTestCase):

    def setUp(self):
        self.post = PostFactory.create(link=reverse('pathology'))
        pathology_list = f.PathologyFactory. \
            create_batch(3, references__articles_count=2)
        self.pathology = pathology_list[0]

    def test_redirect_to_first_pathology(self):
        self.driver.get(self.url_for('home:index'))
        # click on "Post title"
        self.driver.find_element_by_link_text(self.post.title).click()
        # Redirect to first pathology
        self.assertEqual(self.driver.find_element_by_css_selector('h1').text,
                         self.pathology.name)
