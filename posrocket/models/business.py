from uuid import UUID


class BusinessModel:
    id: UUID = None
    sub_domain: str = None
    name: str = None
    type: str = None
    country: str = None
    currency: str = None
    end_of_fiscal_day: str = None
    time_offset: int = None
    phone: str = None
    address: str = None
    image: str = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
