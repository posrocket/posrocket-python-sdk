"""Location Sales Transaction Itemization Python model

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


class SalesTransactionItemizationVariationModel:
    """ mapper class for Sales Transaction Itemization Modifier object from Json Dict

    """
    id: str
    name: str
    pricing_type: str
    external_id: int
    _price_money: LocationInitialMoneyModel

    def __init__(self,
                 id=None,
                 name=None,
                 pricing_type=None,
                 external_id=None,
                 price_money=None,
                 **kwargs
                 ):
        """ map a dict to Sales Transaction Itemization Modifier object

        :param kwargs: Sales Transaction Itemization Modifier json dict
        """
        self.id = id
        self.name = name
        self.pricing_type = pricing_type
        self.external_id = external_id
        self.price_money = price_money

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Itemization Modifier model

        :return: Directory Sales Transaction Itemization Modifier name
        """
        return f'{self.name}'

    @property
    def price_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Itemization Modifier Applied Money
        :return: Sales Transaction Itemization Modifier Applied Money object
        """
        return self._price_money

    @price_money.setter
    def price_money(self, price_money_dict: dict):
        """setter for Sales Transaction Itemization Modifier Applied Money

        :param price_money_dict: json dict for applied money
        :return: None
        """
        if price_money_dict:
            self._price_money = LocationInitialMoneyModel(**price_money_dict)
        else:
            self._price_money = None
