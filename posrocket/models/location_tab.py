"""Location Tab Python model

"""
import datetime
from typing import List

from posrocket.models.catalog_item import CatalogItemModel
from posrocket.models.directory_customer import DirectoryCustomerModel
from posrocket.models.location_order_options import LocationOrderOptionModel
from posrocket.models.location_tab_creator import LocationTabCreatorModel
from posrocket.models.location_tab_item import LocationTabItemModel
from posrocket.models.location_tab_pickup import LocationTabPickupModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ahmad Bazadough, Hamzah Darwish"
__email__ = "a.bazadough@posrocket.com"
__status__ = "Beta"


class LocationTabModel:
    """ mapper class for Location Tab object from Json Dict

    """
    id: str = None
    location_id: str = None
    issuer_id: str = None
    sequence_number: str = None
    name: str = None
    ticket_number: str = None
    creation_time: datetime = None
    status: str = None
    acknowledged: bool = None
    total_amount: float = None
    _order_option: LocationOrderOptionModel = None
    _items: List[LocationTabItemModel] = []
    _customer: DirectoryCustomerModel = None
    _pickup: LocationTabPickupModel = None
    _creator: LocationTabCreatorModel = None

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Tab object

        :param kwargs: Location Tab json dict
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """ String representation for the Location Tab model

        :return: Directory Location Tab name
        """
        return f'{self.name}'

    @property
    def order_option(self) -> LocationOrderOptionModel:
        """
        getter for Tab order option
        :return: Tab order option object
        """
        return self._order_option

    @order_option.setter
    def order_option(self, order_option_dict: dict):
        """setter for Tab order option

        :param order_option_dict: json dict for order option
        :return: None
        """
        self._order_option = LocationOrderOptionModel(**order_option_dict)

    @property
    def items(self) -> List[LocationTabItemModel]:
        """getter for Tab items

        :return: list of items for the Tab
        """
        return self._items

    @items.setter
    def items(self, items_list: List[dict]):
        """setter for Tab items

        :param items_list:json list of item dicts
        :return: None
        """
        self._items = []
        for item in items_list:
            self._items.append(CatalogItemModel(**item))

    @property
    def customer(self) -> DirectoryCustomerModel:
        """
        getter for Tab Customer
        :return: Tab Customer object
        """
        return self._customer

    @customer.setter
    def customer(self, customer_dict: dict):
        """setter for Tab Customer

        :param customer_dict: json dict for Customer
        :return: None
        """
        self._customer = DirectoryCustomerModel(**customer_dict)

    @property
    def pickup(self) -> LocationTabPickupModel:
        """
        getter for Tab Pickup
        :return: Tab Pickup object
        """
        return self._pickup

    @pickup.setter
    def pickup(self, pickup_dict: dict):
        """setter for Tab Pickup

        :param customer_dict: json dict for Pickup
        :return: None
        """
        self._pickup = LocationTabPickupModel(**pickup_dict)

    @property
    def creator(self) -> LocationTabCreatorModel:
        """
        getter for Tab creator
        :return: Tab creator object
        """
        return self._creator

    @creator.setter
    def creator(self, creator_dict: dict):
        """setter for Tab creator

        :param customer_dict: json dict for creator
        :return: None
        """
        self._creator = LocationTabCreatorModel(**creator_dict)
