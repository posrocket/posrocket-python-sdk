class LocationDiscountModel:
    id = None
    name = None
    type = None
    amount = None
    rate = None
    color = None
    pin_required = None
    after_tax = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
