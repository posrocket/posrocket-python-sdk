"""Location Extra Charge Python model

"""
from posrocket.models.location.location_extra_charge_tax import LocationExtraChargeTaxModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
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
    _tax: LocationExtraChargeTaxModel

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Extra Charge object

        :param kwargs: Location Extra Charge json dict
        """

        self.id = None
        self.name = None
        self.type = None
        self.amount = None
        self._tax = None

        for key, value in kwargs.items():
            setattr(self, key, value)

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
