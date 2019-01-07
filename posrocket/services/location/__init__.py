from posrocket.models import LocationModel
from posrocket.utils.requests import Requests


class LocationService(Requests):
    service_url = "/locations"
    model_cls = LocationModel

    def get_locations(self, **kwargs):
        return self.get_list(**kwargs)

    def get_location_by_id(self, pk):
        return self.get_detail(pk)
