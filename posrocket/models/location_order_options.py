from posrocket.models import LocationExtraChargeModel


class LocationOrderOptionModel:
    id = None
    name = None
    _charges = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def charges(self):
        return self._charges

    @charges.setter
    def charges(self, json_charges):
        self._charges = []
        for json_charge in json_charges:
            self._charges.append(LocationExtraChargeModel(**json_charge))
