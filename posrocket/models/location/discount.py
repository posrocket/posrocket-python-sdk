"""Location Discount Python model

"""

from .discount_days import LocationDiscountDaysModel
from posrocket.models.catalog import CatalogItemModel,CatalogCategoryModel
from typing import List
from .location import LocationModel
from datetime import date
__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"

'''
{
#	    "name": "Discount 10%",
#	    "type": "PERCENTAGE", //options: PERCENTAGE/FIXED
#	    "rate": 0.1, //only valid when the type is percentage
#	    "amount": 1000, //only valid when the type is fixed
#	    "locations": [
		"{{location_id}}",
		"{{location_id_2}}",
		"{{location_id_3}}"
	    ],
#    	    "color": "6F7077",
#	    "pin_required": false,
#	    "after_tax": false,
#	    "item_applicable": true,
#	    "automatic": true,
	    "start_date":"2020-10-5T9:00Z",
	    "end_date":"2020-10-15T15:00Z",
	    "days":[
		{
		    "day":"SUNDAY",
		    "time":{
		        "start":"17:00",
		        "end":"21:00"
		    }
		},
		{
		    "day":"FRIDAY",
		    "time":{
		        "start":"17:00",
		        "end":"21:00"
		    }
		}
	    ],
	    "items": ["{{item_id_1}}", "{{item_id_2}}"],
	    "categories": ["{{category_id_1}}", "{{category_id_2}}"]
	}
'''

class LocationDiscountModel:
    """ mapper class for Location Discount object from Json Dict

    """
    id: str
    name: str
    type: str
    amount: float
    rate: float
    color: str
    pin_required: bool
    after_tax: bool
    applied_on: str
    automatic: bool

    item_applicable:bool
    start_date: date
    end_date: date

    _locations:List[LocationModel]
    _items:List[CatalogItemModel]
    _categories:List[CatalogCategoryModel]
    _days:List[LocationDiscountDaysModel]


    # locations:List[str]
    # items:List[str]
    # categories:List[str]
    def __init__(self,
                 id=None,
                 name=None,
                 type=None,
                 amount=None,
                 rate=None,
                 color=None,
                 pin_required=None,
                 after_tax=None,
                 applied_on=None,
                 locations=None,
                 item_applicable=None,
                 automatic=None,
                 start_date=None,
                 end_date=None,
                 items=None,
                 categories=None,
                 days=None,
                 **kwargs
                 ):
        """ map a dict to Location Discount object

        :param kwargs: Location Discount json dict
        """
        self.id = id
        self.name = name
        self.type = type
        self.amount = amount
        self.rate = rate
        self.color = color
        self.pin_required = pin_required
        self.after_tax = after_tax
        self.applied_on = applied_on

        self._locations=locations
        self.item_applicable=item_applicable
        self.automatic=automatic
        self.start_date=start_date
        self.end_date=end_date

        self._items = items
        self._categories = categories
        self._days = days

    def __str__(self) -> str:
        """ String representation for the Location Discount model

        :return: Location Discount name
        """
        return f'{self.name}'


    @property
    def locations(self) -> List[LocationModel]:
        return self._locations

    @property
    def items(self) -> List[CatalogItemModel]:
        return self._items


    @property
    def categories(self) -> List[CatalogCategoryModel]:
        return self._categories

    @property
    def days(self) -> List[LocationDiscountDaysModel]:
        return self._days