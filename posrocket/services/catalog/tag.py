import logging

from posrocket.models.catalog_tag import CatalogTagModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class CatalogTagService(Requests):
    service_url = "/catalog/tags"
    model_cls = CatalogTagModel
    get_tags = BaseServiceFactory.make_list_items_response()
    get_tag_by_id = BaseServiceFactory.make_detail_item_response()
