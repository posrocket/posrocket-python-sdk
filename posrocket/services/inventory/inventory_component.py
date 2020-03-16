"""
Inventory Component Service
"""
import logging

from posrocket.models.inventory import InventoryComponentModel
from posrocket.utils.requests import Requests

__author__ = "Lujain Battikhi, Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Lujain Battikhi", "Rawan Amro"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Lujain Battikhi, Rawan Amro"
__email__ = "launchpad@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class InventoryComponentService(Requests):
    """Inventory Component service class to allow retrieving inventory Component related data
    """
    service_url = "/inventory/components"
    model_cls = InventoryComponentModel

    def get_inventory_components(self, **kwargs):
        return self.get_list(**kwargs)
