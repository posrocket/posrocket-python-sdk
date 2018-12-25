"""Location Sales Transaction Tax Python model

"""
from posrocket.models import LocationInitialMoneyModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class SalesTransactionTaxModel:
    """ mapper class for Sales Transaction Tax object from Json Dict

    """
    id: str
    name: str
    rate: float
    inclusion_type: str
    is_custom_amount: bool
    _applied_money: LocationInitialMoneyModel

    def __init__(self, **kwargs: dict):
        """ map a dict to Sales Transaction Tax object

        :param kwargs: Sales Transaction Tax json dict
        """
        self.id = None
        self.name = None
        self.rate = None
        self.inclusion_type = None
        self.is_custom_amount = None
        self._applied_money = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Tax model

        :return: Directory Sales Transaction Tax name
        """
        return f'{self.name}'

    @property
    def applied_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Tax Applied Money
        :return: Sales Transaction Tax Applied Money object
        """
        return self._applied_money

    @applied_money.setter
    def applied_money(self, applied_money_dict: dict):
        """setter for Sales Transaction Tax Applied Money

        :param applied_money_dict: json dict for applied money
        :return: None
        """
        if applied_money_dict:
            self._applied_money = LocationInitialMoneyModel(**applied_money_dict)
        else:
            self._applied_money = None
