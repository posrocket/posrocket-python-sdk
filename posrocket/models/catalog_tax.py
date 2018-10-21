from uuid import UUID


class CatalogTaxModel:
    id: UUID = None
    name: str = None
    rate: float = None
    inclusion_type: str = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
