"""
Directory Customer Service
"""
import logging

from posrocket.models import DirectoryCustomerModel
from posrocket.services.base_service import BaseServiceFactory
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("pos-python")


class DirectoryCustomerService(Requests):
    """Customer service class to allow retrieving customer related data
    """
    service_url = "/directory/customers/"
    model_cls = DirectoryCustomerModel
    get_customers = BaseServiceFactory.make_list_items_response()
    get_customer_by_id = BaseServiceFactory.make_detail_item_response()

    def create(self, customer: DirectoryCustomerModel):
        """Create new customer in POSRocket Customer Directory

        :param customer: DirectoryCustomerModel type object
        """
        data = {
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "gender": customer.gender,
            "dob": customer.dob,
            "country": customer.country,
            "addresses": [],
            "phone_numbers": []
        }
        for address in customer.addresses:
            data['addresses'].append(
                {
                    "label": address.label,
                    "residence": address.residence,
                    "street": address.street,
                    "building": address.building,
                    "floor": address.floor,
                    "apartment": address.apartment,
                    "extras": address.extras,
                    "is_primary": address.is_primary,
                    "is_verified": address.is_verified,
                    "city": {
                        "id": address.city.id,
                    },
                    "area": {
                        "id": address.area.id,
                    }
                }
            )
        for phone_number in customer.phone_numbers:
            data['phone_numbers'].append(
                {
                    "number": phone_number.number,
                    "is_primary": phone_number.is_primary,
                    "is_verified": phone_number.is_verified,
                }
            )
        print(data)
        response = self.post(self.get_service_url(), data)
        print(response)
        result = self.model_cls(**response['data'])
        return result
