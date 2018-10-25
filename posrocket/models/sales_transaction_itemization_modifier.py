from posrocket.models import LocationInitialMoneyModel


class SalesTransactionItemizationModifierModel:
    id = None
    name = None
    quantity = None
    _applied_money = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def applied_money(self):
        return self._applied_money

    @applied_money.setter
    def applied_money(self, applied_money_dict):
        self._applied_money = LocationInitialMoneyModel(**applied_money_dict)
