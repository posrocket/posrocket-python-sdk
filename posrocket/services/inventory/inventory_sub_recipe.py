"""
Inventory SubRecipe Service
"""
import logging

from posrocket.models.inventory import InventorySubRecipeModel
from posrocket.utils.requests import Requests

__author__ = "Lujain Battikhi, Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Lujain Battikhi", "Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lujain Battikhi, Rawan Amro"
__email__ = "launchpad@posrocket.com"
__status__ = "Beta"


logger = logging.getLogger("posrocket-sdk")


class InventorySubRecipeService(Requests):
    """Inventory Ingredient service class to allow retrieving inventory SubRecipe related data
    """
    service_url = "/inventory/sub-recipes"
    model_cls = InventorySubRecipeModel

    def get_inventory_sub_recipes(self, **kwargs):
        return self.get_list(**kwargs)

    def get_inventory_sub_recipe_by_id(self, pk):
        return self.get_detail(pk)

    def get_inventory_ingredient_activities(self, sub_recipes_id):
        url = self.get_service_url()
        response = self.get(f"{url}/{sub_recipes_id}/activities")
        return InventorySubRecipeModel(**response)
