"""
Catalog Modifier List Service
"""
import logging

from posrocket.models.catalog_modifier_list import CatalogModifierListModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("django")


class CatalogModifierListService(Requests):
    """Modifier List service class to allow retrieving catalog Modifier List related data
    """
    service_url = "/catalog/modifier-lists"
    model_cls = CatalogModifierListModel
    get_modifiers_lists = BaseServiceFactory.make_list_items_response()
    get_modifiers_list_by_id = BaseServiceFactory.make_detail_item_response()
