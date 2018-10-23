import logging

from posrocket.models.catalog_modifier_list import CatalogModifierListModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class CatalogModifierListService(Requests):
    service_url = "/catalog/modifier-lists"
    model_cls = CatalogModifierListModel
    get_modifiers_lists = BaseServiceFactory.make_list_items_response()
    get_modifiers_list_by_id = BaseServiceFactory.make_detail_item_response()
