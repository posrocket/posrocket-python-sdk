import logging

from posrocket.models.catalog_category import CatalogCategoryModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class CatalogCategoryService(Requests):
    service_url = "/locations"
    model_cls = CatalogCategoryModel
    get_items = BaseServiceFactory.make_list_items_response()
    get_item_by_id = BaseServiceFactory.make_detail_item_response()
