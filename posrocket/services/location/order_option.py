"""
Location Order Option Service
"""
import logging

from posrocket.models import LocationOrderOptionModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("django")


class LocationOrderOptionService(LocationRequiredMixin, Requests):
    """Order Option service class to allow retrieving location order option related data
    """
    service_url = "/locations/%s/order-options/"
    model_cls = LocationOrderOptionModel
    get_order_options = BaseServiceFactory.make_list_items_response()
    get_order_option_by_id = BaseServiceFactory.make_detail_item_response()
