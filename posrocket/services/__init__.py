from posrocket.models import LocationModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests
from .business import BusinessService
from .location.tabs import TabService


class LocationService(Requests):
    service_url = "/locations"
    model_cls = LocationModel
    get_locations = BaseServiceFactory.make_list_items_response()
    get_location_by_id = BaseServiceFactory.make_detail_item_response()
