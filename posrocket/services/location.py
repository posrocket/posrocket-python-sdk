from posrocket.models import LocationModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests


class LocationService(Requests):
    service_url = "/locations"
    model_cls = LocationModel
    get_locations = BaseServiceFactory.make_list_items_response()
    get_location_by_id = BaseServiceFactory.make_detail_item_response()
