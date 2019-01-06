"""
Location Discount Service
"""
import logging

from posrocket.models import LocationDiscountModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("django")


class LocationDiscountService(LocationRequiredMixin, Requests):
    """Discount service class to allow retrieving location discount related data
    """
    service_url = "/locations/%s/discounts"
    model_cls = LocationDiscountModel

    def get_discounts(self, **kwargs):
        return self.get_list(**kwargs)

    def get_discount_by_id(self, pk):
        return self.get_detail(pk)
