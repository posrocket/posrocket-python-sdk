class LocationDrawerCreatorModel:
    id = None
    first_name = None
    last_name = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
