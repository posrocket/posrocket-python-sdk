from posrocket.models import LocationInitialMoneyModel


class SalesTransactionTaxModel:
    id = None
    name = None
    rate = None
    inclusion_type = None
    is_custom_amount = None
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
