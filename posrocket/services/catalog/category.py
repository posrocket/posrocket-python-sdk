"""
Catalog Category Service
"""
import logging

from posrocket.models.catalog.category import CatalogCategoryModel
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("django")


class CatalogCategoryService(Requests):
    """Tags service class to allow retrieving catalog category related data
    """
    service_url = "/catalog/categories"
    model_cls = CatalogCategoryModel

    def get_categories(self, **kwargs):
        return self.get_list(**kwargs)

    def get_category_by_id(self, pk):
        return self.get_detail(pk)
