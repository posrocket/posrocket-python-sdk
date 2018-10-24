from posrocket.models.location_tab import TabModel
from posrocket.utils.requests import Requests


class TabService(Requests):
    location_url = "/locations/"

    def get_tabs(self, page=1, location_ids=[]):
        for id in location_ids:
            tab_url = self.location_url + id + '/tabs'
            response = self.get(tab_url, params={
                "page": page
            })
            result = []
            for json_tab in response['data']:
                result.append(TabModel(**json_tab))
            return result\


    def assign_pickup(self, location_id, tab_id, data):
        assign_pickup_url = self.location_url + str(location_id) + '/tabs/' + str(tab_id) + '/assign_pickup/'
        response = self.post(assign_pickup_url, data)
        result = TabModel(**response)
        return result
