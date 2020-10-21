"""
Location Driver Service
"""
from posrocket.models.area_delivery_fees import AreaDeliveryFeesModel
from posrocket.utils.requests import LocationRequiredMixin, Requests

__author__ = "Yazan Alhorani"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Yazan Alhorani"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yazan Alhorani"
__email__ = "Lanuchpad@posrocket.com"
__status__ = "Beta"


class AreaDeliveryFeesModelService(LocationRequiredMixin, Requests):
    """location driver service class to allow retrieving location driver related data
    """
    # locations/{{location_id}}/delivery-costs?area_id={{area_id}}
    service_url = "/locations/%s/delivery-costs"
    model_cls = AreaDeliveryFeesModel

    def get_areas_delivery_fees(self, **kwargs):
        return self.get_list(**kwargs)

    def get_driver_by_id(self, area_id):
        return self.get_with_filter("area_id=" + str(area_id))
