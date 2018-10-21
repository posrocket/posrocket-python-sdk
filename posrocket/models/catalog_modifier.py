from uuid import UUID

from posrocket.models.catalog_pricing import CatalogPricingModel


class CatalogModifierModel:
    id: UUID = None
    name: str = None
    _pricing: list = []

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
