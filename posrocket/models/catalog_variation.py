from uuid import UUID


class CatalogVariationModel:
    id: UUID = None
    name: str = None
    pricing_type: str = None
    barcode: str = None
    sku: str = None
    image: str = None
    pricing: list = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
