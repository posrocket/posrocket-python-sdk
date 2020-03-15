"""Inventory Ingredient Python model

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

from posrocket.models import CatalogCategoryModel
from posrocket.models.inventory.balance import InventoryBalanceModel


class InventoryIngredientModel:
    """mapper class for Inventory Ingredient object from Json Dict

    """
    id: str
    name: str
    description: str
    unit: str
    cost_per_unit: float
    waste_percentage: float
    _category: CatalogCategoryModel
    _balances: List[InventoryBalanceModel]

    def __init__(self, id=None, name=None, description=None, unit=None, cost_per_unit=None, waste_percentage=None, category=None, balances=None,
                 **kwargs):
        """map a dict to Inventory Ingredient object

        :param kwargs: Inventory Ingredient json dict
        """
        self.id = id
        self.name = name
        self.description = description
        self.unit = unit
        self.cost_per_unit = cost_per_unit
        self.waste_percentage = waste_percentage
        self.category = category
        self.balances = balances

    def __str__(self) -> str:
        """ String representation for the Inventory Ingredient model

        :return: Inventory Ingredient name
        """
        return f'{self.name}'

    @property
    def balances(self) -> List[InventoryBalanceModel]:
        """getter for Inventory Ingredient balances

        :return: list of balances for the Inventory Ingredient
        """
        return self._balances

    @balances.setter
    def balances(self, json_balances: List[dict]):
        """setter for Inventory Ingredient balances

        :param json_balances: json list of balance dicts
        :return: None
        """
        self._balances = []
        for json_balance in json_balances or []:
            self._balances.append(InventoryBalanceModel(**json_balance))

    @property
    def category(self) -> CatalogCategoryModel:
        """
        getter for Inventory Ingredient category
        :return: Inventory Ingredient category object
        """
        return self._category

    @category.setter
    def category(self, json_category: dict):
        """setter for Inventory Ingredient category

        :param json_category: json dict for category
        :return: None
        """
        if json_category:
            self._category = CatalogCategoryModel(**json_category)
        else:
            self._category = None
