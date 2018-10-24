import logging

from posrocket.models import LocationDiscountModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests

logger = logging.getLogger("django")


class LocationDiscountService(Requests, LocationRequiredMixin):
    service_url = "/locations/%s/discounts"
    model_cls = LocationDiscountModel
    get_customers = BaseServiceFactory.make_list_items_response()
    get_customer_by_id = BaseServiceFactory.make_detail_item_response()
