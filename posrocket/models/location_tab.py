from uuid import UUID


class TabModel:
    id: UUID = None
    location_id: UUID = None
    issuer_id: UUID = None
    sequence_number: int = None
    name: str = None
    ticket_number: int = None
    creation_time: str = None
    status: str = None
    acknowledged: bool = None
    total_amount: int = None
    order_option: dict = None
    items: dict = None
    customer: dict = None
    pickup: dict = None
    creator: dict = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
