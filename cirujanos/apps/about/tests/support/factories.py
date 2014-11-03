import factory
from faker import Faker
from ....about import models

fake = Faker()


class DoctorFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Doctor

    code = factory.Sequence(lambda n: 'code{0}'.format(n))
    first_name = factory.LazyAttribute(lambda n: fake.first_name())
    last_name = factory.LazyAttribute(lambda n: fake.last_name())
    job = factory.Sequence(lambda n: '{0}'.format(n))
    # email = factory.Sequence(lambda n: 'test{0}@gmail.com'.format(n))

    @factory.post_generation
    def doctorcontents(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for doctor_content in extracted:
                self.doctorcontents.add(doctor_content)


class DoctorContentTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.DoctorContentType

    code = factory.Sequence(lambda n: 'code {0}'.format(n))
    name = factory.Sequence(lambda n: 'name {0}'.format(n))


class DoctorContentFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.DoctorContent

    content_type = factory.SubFactory(DoctorContentTypeFactory)
    content_preview = '<ul><li>Preview 1</li><li>Preview 2</li>'
    content_details = '<ul><li>Details 1</li><li>Details 2</li>'


class NotificationEmailFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.NotificationEmail

    email = factory.Sequence(lambda n: 'email{0}@gmail.com'.format(n))
