"""Inventory Component Python model

"""

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

from posrocket.models.inventory import InventoryCategoryModel


class InventoryComponentModel:
    """mapper class for Inventory Component object from Json Dict

    """
    id: str
    name: str
    type: str
    unit: str
    cost_per_unit: float
    _category: InventoryCategoryModel

    def __init__(self, id=None, name=None, type=None, unit=None, cost_per_unit=None,category=None, **kwargs):
        """map a dict to Inventory Component object

        :param kwargs: Inventory Component json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.unit = unit
        self.cost_per_unit = cost_per_unit
        self.category = category

    def __str__(self) -> str:
        """ String representation for the Inventory Component  model

        :return: Inventory Component name
        """
        return f'{self.name}'

    @property
    def category(self) -> InventoryCategoryModel:
        """
        getter for Inventory Component category
        :return: Inventory component category object
        """
        return self._category

    @category.setter
    def category(self, json_category: dict):
        """setter for Inventory Component category

        :param json_category: json dict for category
        :return: None
        """
        if json_category:
            self._category = InventoryCategoryModel(**json_category)
        else:
            self._category = None
