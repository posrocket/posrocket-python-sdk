"""Inventory Good Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

from typing import List

from posrocket.models.inventory.balance import InventoryBalanceModel


class InventoryGoodModel:
    """mapper class for Inventory Good object from Json Dict

    """
    id: str
    name: str
    object_id: str
    type: str
    unit: str
    cost_per_unit: float
    _balances: List[InventoryBalanceModel]

    def __init__(self, id=None, name=None, object_id=None, type=None, unit=None, cost_per_unit=None,balances=None, **kwargs):
        """map a dict to Inventory Good object

        :param kwargs: Inventory Good json dict
        """
        self.id = id
        self.name = name
        self.object_id = object_id
        self.type = type
        self.unit = unit
        self.cost_per_unit = cost_per_unit
        self.balances = balances

    def __str__(self) -> str:
        """ String representation for the Inventory Good model

        :return: Inventory Good name
        """
        return f'{self.name}'

    @property
    def balances(self) -> List[InventoryBalanceModel]:
        """getter for Good balances

        :return: list of balances for the good
        """
        return self._balances

    @balances.setter
    def balances(self, json_balances: List[dict]):
        """setter for good balances

        :param json_balances: json list of balance dicts
        :return: None
        """
        self._balances = []
        for json_balance in json_balances or []:
            self._balances.append(InventoryBalanceModel(**json_balance))
