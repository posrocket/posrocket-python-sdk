class LocationTabItemModifierModel:
    id = None
    name = None
    quantity = None
    price = None
    order = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'
