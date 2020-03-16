"""
Location Summary Report Service
"""
import logging

from posrocket.models.inventory import InventoryCategoryModel
from posrocket.utils.requests import Requests, LocationRequiredMixin

__author__ = "Lujain Battikhi, Rawan Amro"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Lujain Battikhi", "Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lujain Battikhi, Rawan Amro"
__email__ = "launchpad@posrocket.com"
__status__ = "Beta"


logger = logging.getLogger("posrocket-sdk")


class SummaryReportService(LocationRequiredMixin, Requests):
    """Inventory Category service class to allow retrieving location summary report related data
    """
    service_url = "/locations/%s/end-of-day"
    model_cls = InventoryCategoryModel

    def get_inventory_categories(self, **kwargs):
        return self.get_list(**kwargs)

    def get_inventory_category_by_id(self, pk):
        return self.get_detail(pk)
