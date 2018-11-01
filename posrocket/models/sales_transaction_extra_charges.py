"""Location Sales Transaction Extra Charges Python model

"""
from posrocket.models import SalesTransactionTaxModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class SalesTransactionExtraChargeModel:
    """ mapper class for Sales Transaction Extra Charge object from Json Dict

    """
    id: int = None
    name: str = None
    type: str = None
    rate: float = None
    amount: float = None
    _tax: SalesTransactionTaxModel = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Sales Transaction Extra Charge object

        :param kwargs: Sales Transaction Extra Charge json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Extra Charge model

        :return: Directory Sales Transaction Extra Charge name
        """
        return f'{self.name}'

    @property
    def tax(self) -> SalesTransactionTaxModel:
        """
        getter for Sales Transaction Extra Charge
        :return: Sales Transaction Extra Charge object
        """
        return self._tax

    @tax.setter
    def tax(self, tax_dict: dict):
        """setter for Sales Transaction Extra Charge
Discount
        :param tax_dict: json dict for extra charge
        :return: None
        """
        self._tax = SalesTransactionTaxModel(**tax_dict)
