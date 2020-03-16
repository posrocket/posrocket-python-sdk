"""
Geo Customer Service
"""
import logging

from posrocket.models import CityModel
from posrocket.models.country import CountryModel
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class CountryService(Requests):
    """Country service class to allow retrieving country related data
    """
    service_url = "/countries"
    model_cls = CountryModel

    def get_countries(self, **kwargs):
        return self.get_list(**kwargs)

    def get_country_by_code(self, country_code):
        result = []
        url = self.get_service_url()
        response = self.get(f"{url}/{country_code}")
        logger.info('****************************************************')
        logger.info(response)
        for json_location in response['data']:
            result.append(CityModel(**json_location))
        logger.info('&&&&&&&&&&&&&&&&&&&&&&')
        logger.info(result)
        return result

    def get_country_city_areas(self, country_code, city_id):
        url = self.get_service_url()
        response = self.get(f"{url}/{country_code}/city/{city_id}")
        return CityModel(**response)
