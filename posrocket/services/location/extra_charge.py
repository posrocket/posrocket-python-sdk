"""
Location Extra Charge Service
"""
import logging

from posrocket.models import LocationExtraChargeModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("posrocket-sdk")


class LocationExtraChargeService(LocationRequiredMixin, Requests):
    """Extra Charge service class to allow retrieving location extra charge related data
    """
    service_url = "/locations/%s/extra-charges"
    model_cls = LocationExtraChargeModel

    def get_extra_charges(self, **kwargs):
        return self.get_list(**kwargs)

    def get_extra_charge_by_id(self, pk):
        return self.get_detail(pk)
