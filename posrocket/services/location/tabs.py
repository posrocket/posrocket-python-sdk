from posrocket.models import TabModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import LocationRequiredMixin, Requests


class TabService(Requests, LocationRequiredMixin):
    service_url = "/locations/%s/tabs"
    model_cls = TabModel
    get_tabs = BaseServiceFactory.make_list_items_response()
    get_tab_by_id = BaseServiceFactory.make_detail_item_response()

    def assign_pickup(self, tab_id, data):
        assign_pickup_url = self.get_service_url() + '/' + str(tab_id) + '/assign_pickup/'
        response = self.post(assign_pickup_url, data)
        result = TabModel(**response)
        return result
