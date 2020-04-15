"""
Location Driver Category Service
"""
import logging

from posrocket.models.driver_category import LocationDriverCategoryModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Lujain Battiki, Rawan Amro"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Lujain Battiki, Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lujain Battiki, Rawan Amro"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class LocationDriverCategoryService(LocationRequiredMixin, Requests):
    """location driver category service class to allow retrieving location driver category related data
    """
    service_url = "/locations/%s/delivery/categories"
    model_cls = LocationDriverCategoryModel

    def get_driver_categories(self, **kwargs):
        return self.get_list(**kwargs)

    def get_driver_category_by_id(self, pk):
        return self.get_detail(pk)
