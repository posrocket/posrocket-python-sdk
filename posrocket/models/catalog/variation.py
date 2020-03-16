"""Catalog Variation Python model

"""
from typing import List

from posrocket.models.catalog.pricing import CatalogPricingModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

from posrocket.utils.prices_mixin import PricingMixin


class CatalogVariationModel(PricingMixin):
    """mapper class for Catalog Variation object from Json Dict

    """
    id: str
    name: str
    local_name: str
    pricing_type: str
    barcode: str
    sku: str
    image: str
    _pricing: List[CatalogPricingModel]

    def __init__(self, id=None, name=None, local_name=None, pricing_type=None, barcode=None, sku=None, image=None, pricing=None,
                 **kwargs):
        """map a dict to Catalog Variation object

        :param kwargs: Catalog Variation json dict
        """
        self.id = id
        self.name = name
        self.local_name = local_name
        self.pricing_type = pricing_type
        self.barcode = barcode
        self.sku = sku
        self.image = image
        self.pricing = pricing

    def __str__(self) -> str:
        """ String representation for the Catalog Variation model

        :return: Catalog Variation name
        """
        return f'{self.name}'

    @property
    def pricing(self) -> List[CatalogPricingModel]:
        """getter for Variation pricing

        :return: list of pricing for the Variation
        """
        return self._pricing

    @pricing.setter
    def pricing(self, json_pricing: List[dict]):
        """setter for Variation pricing

        :param json_pricing:json list of pricing dicts
        :return: None
        """
        self._pricing = []
        for json_price in json_pricing or []:
            self._pricing.append(CatalogPricingModel(**json_price))

    def get_price_for_location(self, location_id: str) -> float:
        """return the price for the variation on a specific location

        :param location_id: location id to get the price for
        :return: the price in that location
        """
        for pricing in self._pricing:
            if pricing.location_id == location_id:
                return pricing.price

    def is_available_in_location(self, location_id: str) -> float:
        """return the price for the variation on a specific location

        :param location_id: location id to get the price for
        :return: the price in that location
        """
        for pricing in self._pricing:
            if pricing.location_id == location_id:
                return pricing.available

    @property
    def lowest_price(self) -> float:
        """get the lowest price for the variation between all locations

        :return: the lowest price between all locations
        """
        low = None
        for pricing in self._pricing:
            if not low or pricing.price < low:
                low = pricing.price
        return low

    @property
    def highest_price(self) -> float:
        """get the highest price for the variation between all locations

        :return: the highest price between all locations
        """
        low = None
        for pricing in self._pricing:
            if not low or pricing.price < low:
                low = pricing.price
        return low
