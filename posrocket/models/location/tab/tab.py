"""Location Tab Python model

"""
import datetime
from typing import Dict, List

from posrocket.models import DirectoryAddressModel, DirectoryPhoneModel
from posrocket.models.catalog.item import CatalogItemModel
from posrocket.models.catalog.modifier import CatalogModifierModel
from posrocket.models.catalog.variation import CatalogVariationModel
from posrocket.models.directory.customer import DirectoryCustomerModel, SaleCustomerModel
from posrocket.models.location.order_options import LocationOrderOptionModel
from posrocket.models.location.tab.category import LocationTabCategoryModel
from posrocket.models.location.tab.creator import LocationTabCreatorModel
from posrocket.models.location.tab.custom_amount import LocationTabCustomAmountModel
from posrocket.models.location.tab.item.item import LocationTabItemModel
from posrocket.models.location.tab.pickup import LocationTabPickupModel
from posrocket.models.location.tab.template import LocationTabTemplateModel

__author__ = "Ahmad Bazadough, Hamzah Darwish"
__copyright__ = "Copyright 2019, POSRocket"
__credits__ = ["Ahmad Bazadough", "Hamzah Darwish"]
__license__ = "GPL"
__version__ = "1.0.0"
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
    end_time: datetime
    status: str
    acknowledged: bool
    total_amount: float
    _order_option: LocationOrderOptionModel
    _items: List[LocationTabItemModel]
    _custom_amounts: [LocationTabCustomAmountModel]
    _customer: SaleCustomerModel
    _pickup: LocationTabPickupModel
    _creator: LocationTabCreatorModel
    _category: LocationTabCategoryModel
    _template: LocationTabTemplateModel

    def __init__(self,
                 id=None,
                 location_id=None,
                 issuer_id=None,
                 sequence_number=None,
                 name=None,
                 ticket_number=None,
                 creation_time=None,
                 end_time=None,
                 status=None,
                 acknowledged=None,
                 total_amount=None,
                 order_option=None,
                 items=None,
                 custom_amounts=None,
                 customer=None,
                 pickup=None,
                 creator=None,
                 comments=None,
                 category=None,
                 template=None,
                 **kwargs
                 ):
        """ map a dict to Location Tab object

        :param kwargs: Location Tab json dict
        """
        self.id = id
        self.location_id = location_id
        self.issuer_id = issuer_id
        self.sequence_number = sequence_number
        self.name = name
        self.ticket_number = ticket_number
        self.creation_time = creation_time
        self.end_time = end_time
        self.status = status
        self.acknowledged = acknowledged
        self.total_amount = total_amount
        self.order_option = order_option
        self.items = items
        self.custom_amounts = custom_amounts
        self.customer = customer
        self.pickup = pickup
        self.creator = creator
        self.comments = comments
        self.category = category
        self.template = template

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
        if not order_option_dict:
            self._order_option = None
        elif isinstance(order_option_dict, LocationOrderOptionModel):
            self._order_option = order_option_dict
        else:
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
        for item in items_list or []:
            if type(item) is LocationTabItemModel:
                self._items.append(item)
            else:
                self._items.append(LocationTabItemModel(**item))

    @property
    def custom_amounts(self) -> List[LocationTabCustomAmountModel]:
        """getter for Tab items

        :return: list of items for the Tab
        """
        return self._custom_amounts

    @custom_amounts.setter
    def custom_amounts(self, custom_amounts_list: List[dict]):
        """setter for Tab items

        :param items_list:json list of item dicts
        :return: None
        """
        self._custom_amounts = []
        for custom_amount in custom_amounts_list or []:
            if type(custom_amount) is LocationTabItemModel:
                self._custom_amounts.append(custom_amount)
            else:
                self._items.append(LocationTabItemModel(**custom_amount))

    @property
    def customer(self) -> SaleCustomerModel:
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
        if not customer_dict:
            self._customer = None
        elif type(customer_dict) is DirectoryCustomerModel:
            raise ValueError("Please use set_customer")
        else:
            self._customer = SaleCustomerModel(**customer_dict)

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
        else:
            self._pickup = None

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

    @property
    def category(self) -> LocationTabCategoryModel:
        """
        getter for Tab category
        :return: Tab category object
        """
        return self._category

    @category.setter
    def category(self, category_dict: dict):
        """setter for Tab category

        :param customer_dict: json dict for category
        :return: None
        """
        if category_dict:
            self._category = LocationTabCategoryModel(**category_dict)

    @property
    def template(self) -> LocationTabTemplateModel:
        """
        getter for Tab template
        :return: Tab template object
        """
        return self._template

    @template.setter
    def template(self, template_dict: dict):
        """setter for Tab template

        :param customer_dict: json dict for template
        :return: None
        """
        if template_dict:
            self._template = LocationTabTemplateModel(**template_dict)

    def add_item(self, item: CatalogItemModel, item_quantity: int, notes: str, variation: CatalogVariationModel,
                 modifiers: List[Dict[CatalogModifierModel, int]] = [], custom_discounts=None,
                 discounts=None) -> LocationTabItemModel:
        tab_item = LocationTabItemModel(id=item.id, name=item.name, quantity=item_quantity, notes=notes)
        tab_item.add_variation(variation, self.location_id)
        order = 0
        for modifier in modifiers:
            tab_item.add_modifier(modifier['modifier'], modifier['quantity'], self.location_id, order)
            order += 1
        self.items.append(tab_item)

        for custom_discount in custom_discounts or []:
            tab_item.add_custom_discount(custom_discount)
        for discount in discounts or []:
            tab_item.add_discount(discount)
        return tab_item

    def add_custom_amount(self, name: str, price: int) -> LocationTabCustomAmountModel:
        custom_amount_item = LocationTabCustomAmountModel(name=name, price=price)
        self.custom_amounts.append(custom_amount_item)
        return custom_amount_item

    def set_customer(self, customer: DirectoryCustomerModel, address: DirectoryAddressModel,
                     phone: DirectoryPhoneModel):
        tab_customer = SaleCustomerModel()
        tab_customer.id = customer.id
        tab_customer.first_name = customer.first_name
        tab_customer.last_name = customer.last_name
        tab_customer.email = customer.email
        tab_customer.gender = customer.gender
        tab_customer.dob = customer.dob
        tab_customer.country = customer.country
        tab_customer.address = address
        tab_customer.phone_number = phone
        tab_customer.tags = customer.tags
        self._customer = tab_customer
