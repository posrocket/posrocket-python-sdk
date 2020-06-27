"""Area Python model

"""
from typing import List

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

from posrocket.models import AvenueModel


class AreaModel:
    """ mapper class for Area object from Json Dict

    """
    id: str
    name: str
    _avenues: List[AvenueModel]

    def __init__(self, id=None, name=None, avenues=None, **kwargs):
        """ map a dict to Area object

        :param kwargs: Area json dict
        """
        self.id = id
        self.name = name
        self.avenues = avenues

    def __str__(self) -> str:
        """ String representation for the Area model

        :return: Area name
        """
        return f'{self.name}'

    @property
    def avenues(self) -> List[AvenueModel]:
        """
        getter for Item variations
        :return: list of variations for the item
        """
        return self._avenues

    @avenues.setter
    def avenues(self, json_avenues: List[dict]):

        """setter for item variations

        :param json_variations: json list of variation dicts
        :return: None
        """
        self._areas = []
        for json_avenue in json_avenues or []:
            if json_avenue:
                self._avenues.append(AvenueModel(**json_avenue))
