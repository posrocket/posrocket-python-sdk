import logging

from posrocket.models.catalog_item import CatalogItemModel
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class CatalogItemService(Requests):
    catalog_item_url = "/catalog/items"

    def get_items(self):
        response = self.get(self.catalog_item_url)
        logger.info(response)
        result = []
        for json_location in response['data']:
            result.append(CatalogItemModel(**json_location))
        return result
