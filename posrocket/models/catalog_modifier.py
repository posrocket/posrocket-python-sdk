"""Catalog Modifier Python model

"""
from typing import List

from posrocket.models.catalog_pricing import CatalogPricingModel
from posrocket.utils.prices_mixin import PricingMixin

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class CatalogModifierModel(PricingMixin):
    """mapper class for Catalog Modifier object from Json Dict

    """
    id: str
    name: str
    _pricing: List[CatalogPricingModel]

    def __init__(self, **kwargs):
        """map a dict to Catalog Modifier object

        :param kwargs: Catalog Modifier json dict
        """
        self.id = None
        self.name = None
        self._pricing = []
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Catalog Modifier model

        :return: Catalog Modifier name
        """
        return f'{self.name}'

    @property
    def pricing(self) -> List[CatalogPricingModel]:
        """getter for Modifier pricing

        :return: list of pricing for the Modifier
        """
        return self._pricing

    @pricing.setter
    def pricing(self, json_pricing: List[dict]):
        """setter for Modifier pricing

        :param json_taxes:json list of pricing dicts
        :return: None
        """
        self._pricing = []
        for json_price in json_pricing:
            self._pricing.append(CatalogPricingModel(**json_price))

    def is_available_in_location(self, location_id: str) -> float:
        """return the price for the variation on a specific location

        :param location_id: location id to get the price for
        :return: the price in that location
        """
        for pricing in self._pricing:
            if pricing.location_id == location_id:
                return pricing.available
