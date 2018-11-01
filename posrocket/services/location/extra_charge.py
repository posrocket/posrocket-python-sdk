import logging

from posrocket.models import LocationExtraChargeModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests

logger = logging.getLogger("django")


class LocationExtraChargeService(LocationRequiredMixin, Requests):
    service_url = "/locations/%s/extra-charges"
    model_cls = LocationExtraChargeModel
    get_customers = BaseServiceFactory.make_list_items_response()
    get_customer_by_id = BaseServiceFactory.make_detail_item_response()
