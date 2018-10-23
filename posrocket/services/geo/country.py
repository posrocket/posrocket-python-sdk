import logging

from posrocket.models.country import CountryModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

logger = logging.getLogger("django")


class CountryService(Requests):
    service_url = "/countries"
    model_cls = CountryModel
    get_countries = BaseServiceFactory.make_list_items_response()
    get_tag_by_id = BaseServiceFactory.make_detail_item_response()
