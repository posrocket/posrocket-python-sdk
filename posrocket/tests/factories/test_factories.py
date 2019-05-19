from faker import factory

from posrocket.models import CountryModel


class CountryModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CountryModel
