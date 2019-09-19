from posrocket.models.catalog.item import CatalogItemModel
from posrocket.utils.requests import Requests, LocationRequiredMixin


class LocationItemService(LocationRequiredMixin, Requests):
    """Item service class to allow retrieving catalog item related data
    """
    service_url = "/locations/%s/items"
    model_cls = CatalogItemModel

    def get_items(self, **kwargs):
        return self.get_list(**kwargs)
