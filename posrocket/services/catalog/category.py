"""
Catalog Category Service
"""
import logging

from posrocket.models.catalog_category import CatalogCategoryModel
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


class CatalogCategoryService(Requests):
    """Tags service class to allow retrieving catalog category related data
    """
    service_url = "/catalog/categories"
    model_cls = CatalogCategoryModel
    get_items = BaseServiceFactory.make_list_items_response()
    get_item_by_id = BaseServiceFactory.make_detail_item_response()
