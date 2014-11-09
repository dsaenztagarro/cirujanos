from cirujanos.apps.home import models
import factory


class SliderFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Slider

    name = factory.Sequence(lambda n: 'Slider #{0}'.format(n))
    order = factory.Sequence(lambda n: n)
    enable = True
    content = factory.Sequence(lambda n: 'Content for slider #%s' % n)
