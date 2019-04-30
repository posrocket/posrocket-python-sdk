from unittest import TestCase
from posrocket.tests.factories.test_factories import CountryModelFactory


class TestCountryModel(TestCase):
    def setUp(self):
        self.country_model = CountryModelFactory.build()

    def test_string_rep(self):
        self.assertEqual(u'%s' % self.country_model.name, self.country_model.__str__())
