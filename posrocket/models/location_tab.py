"""Location Tab Python model

"""
import datetime
from typing import Dict, List

from posrocket.models.catalog_item import CatalogItemModel
from posrocket.models.catalog_modifier import CatalogModifierModel
from posrocket.models.catalog_variation import CatalogVariationModel
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
    id: str
    location_id: str
    issuer_id: str
    sequence_number: str
    name: str
    ticket_number: str
    creation_time: datetime
    status: str
    acknowledged: bool
    total_amount: float
    _order_option: LocationOrderOptionModel
    _items: List[LocationTabItemModel]
    _customer: DirectoryCustomerModel
    _pickup: LocationTabPickupModel
    _creator: LocationTabCreatorModel

    def __init__(self, **kwargs: dict):
        """ map a dict to Location Tab object

        :param kwargs: Location Tab json dict
        """
        self.id = None
        self.location_id = None
        self.issuer_id = None
        self.sequence_number = None
        self.name = None
        self.ticket_number = None
        self.creation_time = None
        self.status = None
        self.acknowledged = None
        self.total_amount = None
        self._order_option = None
        self._items = []
        self._customer = None
        self._pickup = None
        self._creator = None

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
        if order_option_dict:
            if isinstance(order_option_dict, LocationOrderOptionModel):
                self._order_option = order_option_dict
            else:
                self._order_option = LocationOrderOptionModel(**order_option_dict)
        else:
            self._order_option = None

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
            if type(item) is LocationTabItemModel:
                self._items.append(item)
            else:
                self._items.append(LocationTabItemModel(**item))

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
        if customer_dict:
            if type(customer_dict) is DirectoryCustomerModel:
                self._customer = customer_dict
            else:
                self._customer = DirectoryCustomerModel(**customer_dict)
        else:
            self._customer = None

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
        if pickup_dict:
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
        if creator_dict:
            self._creator = LocationTabCreatorModel(**creator_dict)

    def add_item(self, item: CatalogItemModel, item_quantity: int, notes: str, variation: CatalogVariationModel,
                 modifiers: List[Dict[CatalogModifierModel, int]] = []) -> LocationTabItemModel:
        tab_item = LocationTabItemModel(id=item.id, name=item.name, quantity=item_quantity, notes=notes)
        tab_item.add_variation(variation, self.location_id)
        for modifier in modifiers:
            tab_item.add_modifier(modifier['modifier'], modifier['quantity'], self.location_id)
        self.items.append(tab_item)
        return tab_item
