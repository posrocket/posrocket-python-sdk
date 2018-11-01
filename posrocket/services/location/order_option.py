import logging

from posrocket.models import LocationOrderOptionModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests

logger = logging.getLogger("django")


class LocationOrderOptionService(LocationRequiredMixin, Requests):
    service_url = "/locations/%s/order-options"
    model_cls = LocationOrderOptionModel
    get_order_options = BaseServiceFactory.make_list_items_response()
    get_order_option_by_id = BaseServiceFactory.make_detail_item_response()
