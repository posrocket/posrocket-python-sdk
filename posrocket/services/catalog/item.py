import logging

from posrocket.models.catalog_item import CatalogItemModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class CatalogItemService(Requests):
    service_url = "/catalog/items"
    model_cls = CatalogItemModel
    get_items = BaseServiceFactory.make_list_items_response()
    get_item_by_id = BaseServiceFactory.make_detail_item_response()
