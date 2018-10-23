from uuid import UUID

from posrocket.models.catalog_pricing import CatalogPricingModel
from posrocket.utils.prices_mixin import PricingMixin


class CatalogVariationModel(PricingMixin):
    id: UUID = None
    name: str = None
    pricing_type: str = None
    barcode: str = None
    sku: str = None
    image: str = None
    _pricing: list = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def pricing(self):
        return self._pricing

    @pricing.setter
    def pricing(self, json_pricing):
        self._pricing = []
        for json_price in json_pricing:
            self._pricing.append(CatalogPricingModel(**json_price))

    def get_price_for_location(self, location_id):
        for pricing in self._pricing:
            if pricing.location_id == location_id:
                return pricing.price

    @property
    def lowest_price(self):
        low = None
        for pricing in self._pricing:
            if not low or pricing.price < low:
                low = pricing.price
        return low

    @property
    def highest_price(self):
        low = None
        for pricing in self._pricing:
            if not low or pricing.price < low:
                low = pricing.price
        return low
