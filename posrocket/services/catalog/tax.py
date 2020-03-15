"""
Catalog Tax Service
"""
import logging

from posrocket.models.catalog.tax import CatalogTaxModel
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class CatalogTaxService(Requests):
    """Tax service class to allow retrieving catalog tax related data
    """
    service_url = "/catalog/taxes"
    model_cls = CatalogTaxModel

    def get_taxes(self, **kwargs):
        return self.get_list(**kwargs)

    def get_tax_by_id(self, pk):
        return self.get_detail(pk)
