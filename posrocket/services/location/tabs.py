"""
Location Tab Service
"""
import logging

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

logger = logging.getLogger("django")


class TabService(LocationRequiredMixin, Requests):
    """Tabs service class to allow retrieving location tab related data
    """
    service_url = "/locations/%s/tabs/"
    model_cls = LocationTabModel
    get_tabs = BaseServiceFactory.make_list_items_response()
    get_tab_by_id = BaseServiceFactory.make_detail_item_response()

    def assign_pickup(self, tab_id, pickup_object):
        """Assign pickup for a Tab

        :param tab_id: POSRocket Tab uuid
        :param data: POSRocket Tab Pickup json dict
        """
        data = {
            "eta": pickup_object.eta,
            "driver_name": pickup_object.driver_name,
            "driver_phone": pickup_object.driver_phone
        }
        assign_pickup_url = self.get_service_url() + '/' + str(tab_id) + '/assign_pickup/'
        response = self.post(assign_pickup_url, data)
        result = self.model_cls(**response)
        return result

    def create(self, tab: LocationTabModel):
        data = {
            "name": tab.name,
            "customer": {"id": tab.customer.id},
            "items": []
        }
        if tab.order_option:
            data['order_option'] = {"id": tab.order_option.id}
        for item in tab.items:
            dict_item = {
                "id": item.id,
                "quantity": item.quantity,
                "variation": {"id": item.variation.id},
                "discounts": [
                    # {"id": "{{discount_id}}"}
                ],
                "modifiers": []
            }
            if item.notes and item.notes != "":
                dict_item["notes"] = item.notes
            for modifier in item.modifiers:
                dict_item['modifiers'].append({
                    "id": modifier.id,
                    "quantity": modifier.quantity,
                    "order": modifier.order
                })
            data['items'].append(dict_item)
        logger.info(data)
        response = self.post(self.get_service_url(), data)
        print(response)
        result = self.model_cls(**response)
        return result
