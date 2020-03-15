"""Inventory Recipe Python model

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

from posrocket.models.inventory import InventoryIngredientModel


class InventoryRecipeModel:
    """mapper class for Inventory Recipe object from Json Dict

    """
    id: str
    name: str
    object_id: str
    type: str
    _ingredients: List[InventoryIngredientModel]

    def __init__(self, id=None, name=None, type=None, object_id=None, ingredients=None, **kwargs):
        """map a dict to Inventory Recipe object

        :param kwargs: Inventory Recipe json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.object_id = object_id
        self.ingredients = ingredients

    def __str__(self) -> str:
        """ String representation for the Inventory Recipe model

        :return: Inventory Recipe name
        """
        return f'{self.name}'

    @property
    def ingredients(self) -> List[InventoryIngredientModel]:
        """getter for Inventory Recipe ingredients

        :return: list of ingredients for the Inventory Recipe
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, json_ingredients: List[dict]):
        """setter for Inventory Recipe ingredient

        :param json_ingredients: json list of ingredient dicts
        :return: None
        """
        self._ingredients = []
        for json_ingredient in json_ingredients or []:
            self._ingredients.append(InventoryIngredientModel(**json_ingredient))
