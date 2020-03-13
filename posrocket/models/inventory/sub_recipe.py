"""Inventory Sub-Recipe Python model

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
from posrocket.models.inventory import InventoryIngredientModel
from posrocket.models.inventory.balance import InventoryBalanceModel


class InventorySubRecipeModel:
    """mapper class for Inventory Sub-Recipe object from Json Dict

    """
    id: str
    name: str
    description: str
    unit: str
    output: float
    cost: float
    cost_per_unit: float
    _category: CatalogCategoryModel
    _balances: List[InventoryBalanceModel]
    _ingredients: List[InventoryIngredientModel]

    def __init__(self, id=None, name=None, type=None, description=None, unit=None, output=None, cost=None,
                 cost_per_unit=None, category=None, balances=None, ingredients=None, **kwargs):
        """map a dict to Inventory Sub-Recipe object

        :param kwargs: Inventory Sub-Recipe json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.unit = unit
        self.output = output
        self.cost = cost
        self.cost_per_unit = cost_per_unit
        self.category = category
        self.balances = balances
        self.ingredients = ingredients

    def __str__(self) -> str:
        """ String representation for the Inventory Sub-Recipe model

        :return: Inventory Sub-Recipe name
        """
        return f'{self.name}'

    @property
    def ingredients(self) -> List[InventoryIngredientModel]:
        """getter for Sub-Recipe ingredients

        :return: list of ingredients for the good
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, json_ingredients: List[dict]):
        """setter for Sub-Recipe ingredient

        :param json_ingredients: json list of ingredient dicts
        :return: None
        """
        self._ingredients = []
        for json_ingredient in json_ingredients or []:
            self._ingredients.append(InventoryIngredientModel(**json_ingredient))

    @property
    def balances(self) -> List[InventoryBalanceModel]:
        """getter for Inventory Sub-Recipe balances

        :return: list of balances for the Inventory Sub-Recipe
        """
        return self._balances

    @balances.setter
    def balances(self, json_balances: List[dict]):
        """setter for Inventory Sub-Recipe balances

        :param json_balances: json list of balance dicts
        :return: None
        """
        self._balances = []
        for json_balance in json_balances or []:
            self._balances.append(InventoryBalanceModel(**json_balance))

    @property
    def category(self) -> CatalogCategoryModel:
        """
        getter for Inventory Sub-Recipe category
        :return: Inventory Sub-Recipe category object
        """
        return self._category

    @category.setter
    def category(self, json_category: dict):
        """setter for Inventory Sub-Recipe category

        :param json_category: json dict for category
        :return: None
        """
        if json_category:
            self._category = CatalogCategoryModel(**json_category)
        else:
            self._category = None
