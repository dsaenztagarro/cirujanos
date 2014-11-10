from cirujanos.tests.support.integration import SeleniumTestCase
from django.core.urlresolvers import reverse
from cirujanos.apps.web.tests.support import factories as f
from cirujanos.apps.home.tests.support.factories import PostFactory


class ProcedureIndexTestCase(SeleniumTestCase):

    def setUp(self):
        self.post = PostFactory.create(link=reverse('procedure'))
        procedure_list = f.ProcedureFactory. \
            create_batch(3, references__articles_count=2)
        self.procedure = procedure_list[0]

    def test_redirect_to_first_procedure(self):
        self.driver.get(self.url_for('home:index'))
        # click on "Post title"
        self.driver.find_element_by_link_text(self.post.title).click()
        # Redirect to first procedure
        self.assertEqual(self.driver.find_element_by_css_selector('h1').text,
                         self.procedure.name)
