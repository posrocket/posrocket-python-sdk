"""
Location Tab Service
"""
import logging

from posrocket.models import LocationTabModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class TabService(LocationRequiredMixin, Requests):
    """Tabs service class to allow retrieving location tab related data
    """
    service_url = "/locations/%s/tabs"
    model_cls = LocationTabModel
    update_service_url = '/locations/%s/tabs/%s/update-tab'
    calculate_service_url = 'locations/%s/tabs/calculate-tab'
    tab_id = None

    def get_tabs(self, **kwargs):
        return self.get_list(**kwargs)

    def get_tab_by_id(self, pk):
        return self.get_detail(pk)

    def assign_pickup(self, tab_id, pickup_object):
        """Assign pickup for a Tab

        :param tab_id: POSRocket Tab uuid
        :param data: POSRocket Tab Pickup json dict
        """
        data = {"eta": pickup_object.eta, "driver_name": pickup_object.driver_name,
                "driver_phone": pickup_object.driver_phone}
        assign_pickup_url = f"{self.get_service_url()}/{str(tab_id)}/assign_pickup"
        response = self.post(assign_pickup_url, data)
        result = self.model_cls(**response)
        return result

    def cancel(self, tab: LocationTabModel):
        """Assign pickup for a Tab

        :param tab: POSRocket Tab
        """
        cancel_tab_url = f"{self.get_service_url()}/{str(tab.id)}/cancel"
        response = self.post(cancel_tab_url, {})
        result = self.model_cls(**response)
        return result

    def create(self, tab: LocationTabModel):
        data = self.prepare_payload(tab)
        logger.info("----- Create Tab -----")
        logger.info(data)
        response = self.post(self.get_service_url(), data)
        result = self.model_cls(**response)
        return result

    def update(self, tab: LocationTabModel):
        data = self.prepare_payload(tab)
        data['status'] = tab.status
        del data['delivery']
        logger.info("updated data:")
        logger.info(data)
        response = self.post(self.get_update_service_url(), data)
        result = self.model_cls(**response)
        return result

    def calculate(self, tab: LocationTabModel):
        data = self.prepare_payload(tab)
        data['status'] = tab.status
        del data['delivery']
        logger.info("calculated data:")
        logger.info(data)
        response = self.post(self.get_calculate_service_url(), data)
        result = response
        return result

    @staticmethod
    def prepare_payload(tab):
        data = {"name": tab.name,
                "customer": {"id": tab.customer.id, "phone_number": {"id": tab.customer.phone_number.id}}, "items": [],
                "custom_amount": [], "external_fees": [], "delivery": {}, "comments": tab.comments, "notes": tab.notes}
        data['payment_methods']=[]
        if tab.payment_methods and len(tab.payment_methods)>0:
            for payment_method_id in tab.payment_methods:
                data['payment_methods'].append({"id":payment_method_id,"name":"xxxxxxxxxxxxxxx"})
        if tab.customer.address:
            data["customer"]["address"] = {"id": tab.customer.address.id}
        if tab.order_option:
            data['order_option'] = {"id": tab.order_option.id}
        for external_fee in tab.external_fees:
            external_fee_obj = {'name': external_fee.name, 'type': external_fee.fees_type,
                                'amount': external_fee.amount, 'is_locked': external_fee.is_locked,
                                'is_disabled': external_fee.is_disabled, 'id': str(external_fee.id)}
            data['external_fees'].append(external_fee_obj)
        if not data['external_fees']:
            del data['external_fees']
        for item in tab.items:
            dict_item = {"id": item.id, "quantity": item.quantity, "variation": {"id": item.variation.id},
                         "discounts": [  # # {"id": "{{discount_id}}"}
                         ], "custom_discounts": [  # {"id": "{{discount_id}}"}
                ], "modifiers": []}
            if item.notes and item.notes != "":
                dict_item["notes"] = item.notes
            for modifier in item.modifiers:
                dict_item['modifiers'].append(
                    {"id": modifier.id, "quantity": modifier.quantity, "order": modifier.order})

            for custom_discount in item.custom_discounts:
                tmp_discount = {"name": custom_discount.name, "type": custom_discount.type, }
                if custom_discount.value:
                    tmp_discount['value'] = custom_discount.value
                if custom_discount.rate:
                    tmp_discount['rate'] = custom_discount.rate
                dict_item['custom_discounts'].append(tmp_discount)

            for discount in item.discounts:
                dict_item['discounts'].append(
                    {"id": discount.id, "applied_on": discount.applied_on if discount.applied_on else "ITEM"})
            data['items'].append(dict_item)
        for custom_amounts in tab.custom_amounts:
            data['custom_amount'].append({"name": custom_amounts.name, "price": custom_amounts.price})
        return data
