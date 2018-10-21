from uuid import UUID


class CatalogPricingModel:
    id: UUID = None
    location_id: UUID = None
    price: int = None
    has_inventory_cost: bool = None
    available: bool = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
