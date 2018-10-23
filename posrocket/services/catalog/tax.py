import logging

from posrocket.models.catalog_tax import CatalogTaxModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class CatalogTaxService(Requests):
    service_url = "/catalog/tags"
    model_cls = CatalogTaxModel
    get_taxes = BaseServiceFactory.make_list_items_response()
    get_tax_by_id = BaseServiceFactory.make_detail_item_response()
