from cirujanos.apps.home import models
import factory
import os


TEST_IMAGE_PATH = os.path.join(os.path.dirname(__file__), '..', 'fixtures',
                               'images')
TEST_POST_IMAGE_PATH = os.path.join(TEST_IMAGE_PATH, 'post_dummy.png')


class SliderFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Slider

    name = factory.Sequence(lambda n: 'Slider #{0}'.format(n))
    order = factory.Sequence(lambda n: n)
    enable = True
    content = factory.Sequence(lambda n: 'Content for slider #%s' % n)


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Post

    order = factory.Sequence(lambda n: n)
    public = True
    is_system = False
    system_image_path = None
    image = factory.django.ImageField(from_path=TEST_POST_IMAGE_PATH)
    title = factory.Sequence(lambda n: 'Post ##{0}'.format(n))
    description = factory.Sequence(
        lambda n: 'Long description for post ##{0}'.format(n))
    link = '#'
