from posrocket.models import BusinessModel
from posrocket.utils.requests import Requests


class BusinessService(Requests):
    business_url = "/business"

    def get_business_info(self):
        response = self.get(self.business_url)
        business = BusinessModel(**response)
        return business
