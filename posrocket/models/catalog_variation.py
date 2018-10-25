from posrocket.models import CatalogPricingModel
from posrocket.utils.prices_mixin import PricingMixin


class CatalogVariationModel(PricingMixin):
    id = None
    name = None
    pricing_type = None
    barcode = None
    sku = None
    image = None
    _pricing = None

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
