from posrocket.models.location_extra_charge_tax import LocationExtraChargeTaxModel


class LocationExtraChargeModel:
    id = None
    name = None
    type = None
    amount = None
    _tax = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, json_tax):
        self._tax = LocationExtraChargeTaxModel(**json_tax)
