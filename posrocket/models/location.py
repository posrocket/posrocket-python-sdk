from uuid import UUID


class LocationModel:
    id: UUID = None
    name: str = None
    tax_number: str = None
    phone: str = None
    address: str = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
