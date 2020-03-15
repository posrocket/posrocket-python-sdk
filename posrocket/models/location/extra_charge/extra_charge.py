"""Location Extra Charge Python model

"""
from posrocket.models.location.extra_charge.tax import LocationExtraChargeTaxModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationExtraChargeModel:
    """ mapper class for Location Extra Charge object from Json Dict

    """
    id: str
    name: str
    type: str
    amount: float
    rate: float
    _tax: LocationExtraChargeTaxModel

    def __init__(self, id=None, name=None, type=None, amount=None, rate=None, tax=None, **kwargs):
        """ map a dict to Location Extra Charge object

        :param kwargs: Location Extra Charge json dict
        """

        self.id = id
        self.name = name
        self.type = type
        self.amount = amount
        self.rate = rate
        self.tax = tax

    def __str__(self) -> str:
        """ String representation for the Location Extra Charge model

        :return: Directory Location Extra Charge name
        """
        return f'{self.name}'

    @property
    def tax(self) -> LocationExtraChargeTaxModel:
        """
        getter for Extra Charge Tax
        :return: Extra Charge Tax object
        """
        return self._tax

    @tax.setter
    def tax(self, json_tax: dict):
        """setter for Extra Charge Tax

        :param json_tax: json dict for Tax
        :return: None
        """
        if json_tax:
            self._tax = LocationExtraChargeTaxModel(**json_tax)
        else:
            self._tax = None
