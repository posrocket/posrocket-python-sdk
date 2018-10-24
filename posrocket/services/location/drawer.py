import logging

from posrocket.models import LocationDrawerModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests

logger = logging.getLogger("django")


class LocationDrawerService(Requests, LocationRequiredMixin):
    service_url = "/location/%s/drawers"
    model_cls = LocationDrawerModel
    get_customers = BaseServiceFactory.make_list_items_response()
    get_customer_by_id = BaseServiceFactory.make_detail_item_response()
