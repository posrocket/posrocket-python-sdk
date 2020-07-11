"""Location Tab Python model

"""
import datetime
from typing import Dict, List

from posrocket.models import DirectoryAddressModel, DirectoryPhoneModel
from posrocket.models.catalog.item import CatalogItemModel
from posrocket.models.catalog.modifier import CatalogModifierModel
from posrocket.models.catalog.variation import CatalogVariationModel
from posrocket.models.directory.customer import DirectoryCustomerModel, SaleCustomerModel
from posrocket.models.external_fees import ExternalFeesModel
from posrocket.models.location.delivery import DeliveryModel
from posrocket.models.location.order_options import LocationOrderOptionModel
from posrocket.models.location.tab.category import LocationTabCategoryModel
from posrocket.models.location.tab.creator import LocationTabCreatorModel
from posrocket.models.location.tab.custom_amount import LocationTabCustomAmountModel
from posrocket.models.location.tab.item.item import LocationTabItemModel
from posrocket.models.location.tab.pickup import LocationTabPickupModel
from posrocket.models.location.tab.template import LocationTabTemplateModel

__author__ = "Yazan Alhorani"
__copyright__ = "Copyright 2020, POSRocket"
__credits__ = ["Yazan Alhorani"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yazan alhorani"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


# {
#     "name": "CC#188: rawan amro",
#     "session_time": 0.0,
#     "inclusive_tax": 0.0,
#     "discount": 0.0,
#     "tax": 0.0,
#     "extra_charge": 0.0,
#     "total": 0.0,
#     "taxes": [],
#     "extra_charges": [],
#     "external_fees": [],
#     "itemization": [
#         {
#             "id": "a23267b5-848e-4645-a365-4a24c83e17c4",
#             "name": "AA",
#             "quantity": 1,
#             "discount": 0,
#             "gross_sales": 0,
#             "net_sales": 0,
#             "total": 0,
#             "variation": {
#                 "id": "a2c83b0f-415f-4bc9-a239-0c68744f02f4",
#                 "name": "AA",
#                 "price": 0
#             },
#             "discounts": [
#                 {
#                     "id": "7ef121b8-1c69-4267-ad7d-7641e49f458a",
#                     "name": "test2",
#                     "type": "PERCENTAGE",
#                     "rate": 0.3,
#                     "amount": 0.0,
#                     "value": 0.0,
#                     "applied_on": "SALE"
#                 }
#             ],
#             "modifiers": [],
#             "taxes": []
#         }
#     ]
# }


class SaleCalculationModel:
    """ mapper class for Location Tab object from Json Dict

    """
    id: str
    discount: float
    tax: float
    extra_charge: float
    total: float

    def __init__(self, id=None, tax=None, discount=None, extra_charge=None, total=None, **kwargs):
        """ map a dict to Location Tab object

        :param kwargs: Location Tab json dict
        """
        self.id = id
        self.discount = discount
        self.tax = tax
        self.extra_charge = extra_charge
        self.total = total

    def __str__(self) -> str:
        """ String representation for the Location Tab model

        :return: Directory Location Tab name
        """
        return f'{self.id}'

