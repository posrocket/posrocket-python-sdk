"""
Location Drawer Service
"""
import logging

from posrocket.models import LocationDrawerModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

logger = logging.getLogger("django")


class LocationDrawerService(LocationRequiredMixin, Requests):
    """Drawer service class to allow retrieving location drawer related data
    """
    service_url = "/locations/%s/drawers/"
    model_cls = LocationDrawerModel

    def get_drawers(self, **kwargs):
        return self.get_list(**kwargs)

    def get_drawer_by_id(self, pk):
        return self.get_detail(pk)
