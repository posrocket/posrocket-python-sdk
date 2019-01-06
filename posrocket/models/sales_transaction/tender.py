"""Location Sales Transaction Tender Python model

"""
from posrocket.models import LocationInitialMoneyModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class SalesTransactionTenderModel:
    """ mapper class for Sales Transaction Tender object from Json Dict

    """
    type: str
    name: str
    card_brand: str
    _total_money: LocationInitialMoneyModel

    def __init__(self,
                 type=None,
                 name=None,
                 card_brand=None,
                 total_money=None,
                 **kwargs
                 ):
        """ map a dict to Sales Transaction Tender object

        :param kwargs: Sales Transaction Tender json dict
        """
        self.type = type
        self.name = name
        self.card_brand = card_brand
        self.total_money = total_money

    def __str__(self):
        return f'{self.name}'

    @property
    def total_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Tender Total Money
        :return: Sales Transaction Tender Total Money object
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money_dict: dict):
        """setter for Sales Transaction Tender Total Money

        :param total_money_dict: json dict for tender total money
        :return: None
        """
        if total_money_dict:
            self._total_money = LocationInitialMoneyModel(**total_money_dict)
        else:
            self._total_money = None
