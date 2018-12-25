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

    def get_customers(self, **kwargs):
        return self.get_list(**kwargs)

    def get_customer_by_id(self, pk):
        return self.get_detail(pk)

    def create(self, customer: DirectoryCustomerModel):
        """Create new customer in POSRocket Customer Directory

        :param customer: DirectoryCustomerModel type object
        """
        data = self.prepare_payload(customer)
        print(data)
        response = self.post(self.get_service_url(), data)
        print(response)
        result = self.model_cls(**response['data'])
        return result

    def update(self, customer: DirectoryCustomerModel):
        """Create new customer in POSRocket Customer Directory

        :param customer: DirectoryCustomerModel type object
        """
        data = self.prepare_payload(customer)
        logger.info(data)
        response = self.put(f"{self.get_service_url()}{customer.id}/", data)
        logger.info(response)
        result = self.model_cls(**response['data'])
        return result

    def prepare_payload(self, customer):
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
            tmp_address = {
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
            if address.id:
                tmp_address["id"] = address.id
            data['addresses'].append(
                tmp_address
            )
        for phone_number in customer.phone_numbers:
            tmp_phone = {
                "number": phone_number.number,
                "is_primary": phone_number.is_primary,
                "is_verified": phone_number.is_verified,
            }
            if phone_number.id:
                tmp_phone['id'] = phone_number.id
            data['phone_numbers'].append(tmp_phone)
        logger.info(data)
        return data
