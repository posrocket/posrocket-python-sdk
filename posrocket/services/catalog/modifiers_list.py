"""
Catalog Modifier List Service
"""
import logging

from posrocket.models.catalog.modifier_list import CatalogModifierListModel
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
    service_url = "/catalog/modifier-lists/"
    model_cls = CatalogModifierListModel

    def get_modifiers_lists(self, **kwargs):
        return self.get_list(**kwargs)

    def get_modifiers_list_by_id(self, pk):
        return self.get_detail(pk)
