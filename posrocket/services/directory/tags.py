import logging

from posrocket.models import DirectoryTagModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class DirectoryCustomerService(Requests):
    service_url = "/directory/tags"
    model_cls = DirectoryTagModel
    get_customers = BaseServiceFactory.make_list_items_response()
    get_customer_by_id = BaseServiceFactory.make_detail_item_response()
