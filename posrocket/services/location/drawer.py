import logging

from posrocket.models import LocationDrawerModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests

logger = logging.getLogger("django")


class LocationDrawerService(LocationRequiredMixin, Requests):
    service_url = "/locations/%s/drawers"
    model_cls = LocationDrawerModel
    get_drawers = BaseServiceFactory.make_list_items_response()
    get_drawer_by_id = BaseServiceFactory.make_detail_item_response()
