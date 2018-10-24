class LocationDrawerPaymentMethodModel:
    id = None
    name = None
    label = None
    type = None
    sales = None
    refunds = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.type}'
