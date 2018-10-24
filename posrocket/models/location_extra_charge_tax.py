class LocationExtraChargeTaxModel:
    id = None
    name = None
    inclusion_type = None
    rate = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
