from posrocket.models import LocationTabModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests


class TabService(LocationRequiredMixin, Requests):
    service_url = "/locations/%s/tabs/"
    model_cls = LocationTabModel
    get_tabs = BaseServiceFactory.make_list_items_response()
    get_tab_by_id = BaseServiceFactory.make_detail_item_response()

    def assign_pickup(self, tab_id, data):
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
                "notes": item.notes,
                "variation": {"id": item.variation.id},
                "discounts": [
                    # {"id": "{{discount_id}}"}
                ],
                "modifiers": []
            }
            for modifier in item.modifiers:
                dict_item['modifiers'].append({
                    "id": modifier.id,
                    "quantity": modifier.quantity,
                    "order": modifier.order
                })
            data['items'].append(dict_item)
        print(data)
        response = self.post(self.get_service_url(), data)
        print(response)
        result = self.model_cls(**response['data'])
        return result
