class LocationDrawerPaymentModel:
    id = None
    type = None
    amount = None
    description = None
    time = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.type}'
