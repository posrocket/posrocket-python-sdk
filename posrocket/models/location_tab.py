from posrocket.models import LocationOrderOptionModel, CatalogItemModel, DirectoryCustomerModel, \
    LocationTabCreatorModel, LocationTabPickupModel


class LocationTabModel:
    id = None
    location_id = None
    issuer_id = None
    sequence_number = None
    name = None
    ticket_number = None
    creation_time = None
    status = None
    acknowledged = None
    total_amount = None
    _order_option = None
    _items = []
    _customer = None
    _pickup = None
    _creator = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.name}'

    @property
    def order_option(self):
        return self._order_option

    @order_option.setter
    def order_option(self, order_option_dict):
        self._order_option = LocationOrderOptionModel(**order_option_dict)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items_list):
        self._items = []
        for item in items_list:
            self._items.append(CatalogItemModel(**item))

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer_dict):
        self._customer = DirectoryCustomerModel(**customer_dict)

    @property
    def pickup(self):
        return self._pickup

    @pickup.setter
    def pickup(self, pickup_dict):
        self._pickup = LocationTabPickupModel(**pickup_dict)

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, creator_dict):
        self._creator = LocationTabCreatorModel(**creator_dict)
