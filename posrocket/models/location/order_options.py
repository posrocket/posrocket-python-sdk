"""Location Order Option Python model

"""
from typing import List

from posrocket.models import LocationExtraChargeModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationOrderOptionModel:
    """ mapper class for Location Order Option object from Json Dict

    """
    id: str
    name: str
    _charges: List[LocationExtraChargeModel]

    def __init__(self,
                 id=None,
                 name=None,
                 charges=None
                 ):
        """ map a dict to Location Order Option object

        :param kwargs: Location Order Option json dict
        """
        self.id = id
        self.name = name
        self.charges = charges

    def __str__(self) -> str:
        """ String representation for the Location Order Option model

        :return: Directory Location Order Option name
        """
        return f'{self.name}'

    @property
    def charges(self) -> List[LocationExtraChargeModel]:
        """getter for Order Option charges

        :return: list of charges for the Order Option
        """
        return self._charges

    @charges.setter
    def charges(self, json_charges: List[dict]):
        """setter for Order Option charges

        :param json_charges:json list of charge dicts
        :return: None
        """
        self._charges = []
        for json_charge in json_charges or []:
            self._charges.append(LocationExtraChargeModel(**json_charge))
