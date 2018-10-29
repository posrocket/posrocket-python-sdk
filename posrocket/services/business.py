"""
Business Service
"""
from posrocket.models import BusinessModel
from posrocket.utils.requests import Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class BusinessService(Requests):
    """Business service class to allow retrieving data for connected Business
    """
    business_url = "/business"

    def get_business_info(self):
        """Get Business info for connected Business
        
        """
        response = self.get(self.business_url)
        business = BusinessModel(**response)
        return business
