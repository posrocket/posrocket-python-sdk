"""
Location Register Service
"""
import logging

from posrocket.models.location.register import LocationRegisterModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class LocationRegisterService(LocationRequiredMixin, Requests):
    """Register service class to allow retrieving location register related data
    """
    service_url = "/locations/%s/registers"
    model_cls = LocationRegisterModel

    def get_registers(self, **kwargs):
        return self.get_list(**kwargs)

    def get_register_by_id(self, pk):
        return self.get_detail(pk)
