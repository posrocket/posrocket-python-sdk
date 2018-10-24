class LocationModel:
    id = None
    name = None
    tax_number = None
    phone = None
    address = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
