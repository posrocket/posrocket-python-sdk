"""
Location Tab Service
"""
from posrocket.models import LocationTabModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class TabService(Requests, LocationRequiredMixin):
    """Tabs service class to allow retrieving location tab related data
    """
    service_url = "/locations/%s/tabs"
    model_cls = LocationTabModel
    get_tabs = BaseServiceFactory.make_list_items_response()
    get_tab_by_id = BaseServiceFactory.make_detail_item_response()

    def assign_pickup(self, order_id, data):
        """Assign pickup for an Order

        :param order_id: POSRocket Order uuid
        :param data: POSRocket Order Pickup json dict
        """
        assign_pickup_url = self.get_service_url() + '/' + str(order_id) + '/assign_pickup/'
        response = self.post(assign_pickup_url, data)
        result = self.model_cls(**response)
        return result
