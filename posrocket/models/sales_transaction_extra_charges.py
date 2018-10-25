from posrocket.models import SalesTransactionTaxModel


class SalesTransactionExtraChargeModel:
    id = None
    name = None
    type = None
    rate = None
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
    def tax(self, tax_dict):
        self._tax = SalesTransactionTaxModel(**tax_dict)
