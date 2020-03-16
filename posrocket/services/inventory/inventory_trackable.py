"""
Inventory Trackables Service
"""
import logging

from posrocket.models.inventory import InventoryTrackableModel
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


class InventoryTrackableService(Requests):
    """Inventory Ingredient service class to allow retrieving inventory Trackable related data
    """
    service_url = "/inventory/trackables"
    model_cls = InventoryTrackableModel

    def get_inventory_trackables(self, **kwargs):
        return self.get_list(**kwargs)
