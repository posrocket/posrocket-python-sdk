from posrocket.models import LocationModel
from posrocket.utils.requests import Requests


class LocationService(Requests):
    location_url = "/locations"

    def get_locations(self, page=1):
        response = self.get(self.location_url, params={
            "page": page
        })
        result = []
        for json_location in response['data']:
            result.append(LocationModel(**json_location))
        return result
