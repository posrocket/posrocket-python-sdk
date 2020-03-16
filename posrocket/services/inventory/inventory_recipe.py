"""
Inventory Recipe Service
"""
import logging

from posrocket.models.inventory import InventoryRecipeModel
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


class InventoryRecipeService(Requests):
    """Inventory Ingredient service class to allow retrieving inventory Recipe related data
    """
    service_url = "/inventory/recipes"
    model_cls = InventoryRecipeModel

    def get_inventory_recipes(self, **kwargs):
        return self.get_list(**kwargs)

    def get_inventory_recipe_by_id(self, pk):
        return self.get_detail(pk)