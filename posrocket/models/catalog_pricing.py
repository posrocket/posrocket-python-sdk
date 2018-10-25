class CatalogPricingModel:
    id = None
    location_id = None
    price = None
    has_inventory_cost = None
    available = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
