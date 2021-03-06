"""
Inventory Good Service
"""
import logging

from posrocket.models.inventory import InventoryGoodModel
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


class InventoryGoodService(Requests):
    """Inventory Good service class to allow retrieving inventory good related data
    """
    service_url = "/inventory/goods"
    model_cls = InventoryGoodModel

    def get_inventory_goods(self, **kwargs):
        return self.get_list(**kwargs)

    def get_inventory_good_by_id(self, pk):
        return self.get_detail(pk)

    def get_inventory_good_activities(self, good_id):
        url = self.get_service_url()
        response = self.get(f"{url}/{good_id}/activities")
        return InventoryGoodModel(**response)
