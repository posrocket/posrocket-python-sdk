"""Location Sales Transaction Extra Charges Python model

"""
import logging

from posrocket.models import LocationInitialMoneyModel
from posrocket.models.sales_transaction.tax import SalesTransactionTaxModel

logger = logging.getLogger("posrocket-sdk")

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class SalesTransactionExtraChargeModel:
    """ mapper class for Sales Transaction Extra Charge object from Json Dict

    """
    id: str
    name: str
    type: str
    rate: float
    amount: float
    _tax: SalesTransactionTaxModel

    # _applied_money: LocationInitialMoneyModel
    # _total_money: LocationInitialMoneyModel

    def __init__(self,
                 id=None,
                 name=None,
                 type=None,
                 rate=None,
                 amount=None,
                 tax=None,
                 applied_money=None,
                 total_money=None,
                 **kwargs
                 ):
        """ map a dict to Sales Transaction Extra Charge object

        :param kwargs: Sales Transaction Extra Charge json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.rate = rate
        self.amount = amount
        self.tax = tax
        self.applied_money = applied_money
        self.total_money = total_money

    def __str__(self) -> str:
        """ String representation for the Sales Transaction Extra Charge model

        :return: Directory Sales Transaction Extra Charge name
        """
        return f'{self.name}'

    @property
    def tax(self) -> SalesTransactionTaxModel:
        """
        getter for Sales Transaction Extra Charge Tax
        :return: Sales Transaction Extra Charge Tax object
        """
        return self._tax

    @tax.setter
    def tax(self, tax_dict: dict):
        """setter for Sales Transaction Extra Charge Tax
        :param tax_dict: json dict for extra charge tax
        :return: None
        """
        if tax_dict:
            self._tax = SalesTransactionTaxModel(**tax_dict)
        else:
            self._tax = None

    @property
    def applied_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Extra Charge Applied Money
        :return: Sales Transaction Extra Charge Applied Money object
        """
        return self._applied_money

    @applied_money.setter
    def applied_money(self, applied_money_dict: dict):
        """setter for Sales Transaction Extra Charge Applied Money
        :param applied_money_dict: json dict for extra charge applied money
        :return: None
        """
        if applied_money_dict:
            self._applied_money = LocationInitialMoneyModel(**applied_money_dict)
        else:
            self._applied_money = None

    @property
    def total_money(self) -> LocationInitialMoneyModel:
        """
        getter for Sales Transaction Extra Charge Total Money
        :return: Sales Transaction Extra Charge Total Money object
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money_dict: dict):
        """setter for Sales Transaction Extra Charge Total Money
        :param total_money_dict: json dict for extra charge total money
        :return: None
        """
        if total_money_dict:
            self._total_money = LocationInitialMoneyModel(**total_money_dict)
        else:
            self._total_money = None
