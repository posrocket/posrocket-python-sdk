"""Location Sales Transaction Itemization Python model

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


class SalesTransactionItemizationModifierModel:
    """ mapper class for Sales Transaction Itemization Modifier object from Json Dict

    """
    id: str
    name: str
    quantity: int
    _applied_money: LocationInitialMoneyModel

    def __init__(self, **kwargs: dict):
        """ map a dict to Sales Transaction Itemization Modifier object

        :param kwargs: Sales Transaction Itemization Modifier json dict
        """
        self.id = None
        self.name = None
        self.quantity = None
        self._applied_money = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Itemization Modifier model

        :return: Directory Sales Transaction Itemization Modifier name
        """
        return f'{self.name}'

    @property
    def applied_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Itemization Modifier Applied Money
        :return: Sales Transaction Itemization Modifier Applied Money object
        """
        return self._applied_money

    @applied_money.setter
    def applied_money(self, applied_money_dict: dict):
        """setter for Sales Transaction Itemization Modifier Applied Money

        :param applied_money_dict: json dict for applied money
        :return: None
        """
        self._applied_money = LocationInitialMoneyModel(**applied_money_dict)
