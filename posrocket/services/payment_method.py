"""
Catalog Category Service
"""
import logging

from posrocket.models.payment_method import PaymentMethodModel
from posrocket.utils.requests import Requests

__author__ = "Lujain Battikhi"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Lujain Battikhi"]
__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Lujain Battikhi"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class PaymentMethodService(Requests):
    """Tags service class to allow retrieving catalog category related data
    """
    service_url = "/me/payment-methods"
    model_cls = PaymentMethodModel

    def get_payment_methods(self, **kwargs):
        return self.get_list(**kwargs)

    def get_payment_method_by_id(self, pk):
        return self.get_detail(pk)
