"""
Location Driver Service
"""

from posrocket.models.driver import LocationDriverModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Lujain Battiki, Rawan Amro"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Lujain Battiki, Rawan Amro"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lujain Battiki, Rawan Amro"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"


class LocationDriverService(LocationRequiredMixin, Requests):
    """location driver service class to allow retrieving location driver related data
    """
    service_url = "/locations/%s/delivery/drivers"
    model_cls = LocationDriverModel

    def get_drivers(self, **kwargs):
        return self.get_list(**kwargs)

    def get_driver_by_id(self, pk):
        return self.get_detail(pk)
